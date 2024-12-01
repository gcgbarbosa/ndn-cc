from minindn.app import NDNConsumerApp

class CustomConsumer(NDNConsumerApp):
    def __init__(self):
        super().__init__()
        self.interest_rate = 10  # Initial Interest packets per second

    def on_data(self, data):
        if 'ECN' in data.name:
            print("ECN Mark Received. Reducing Interest rate.")
            self.interest_rate = max(1, self.interest_rate - 2)
        else:
            print("Data received. Adjusting Interest rate.")
            self.interest_rate += 1

        self.send_interests()

    def send_interests(self):
        for _ in range(self.interest_rate):
            self.send_interest(f'/test/data')
