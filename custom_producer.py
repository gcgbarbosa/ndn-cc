from minindn.app import NDNProducerApp

class CustomProducer(NDNProducerApp):
    def __init__(self):
        super().__init__()
        self.production_rate = 10  # Packets per second

    def on_interest(self, interest):
        if 'ECN' in interest.name:
            print("ECN Mark detected. Reducing production rate.")
            self.production_rate = max(1, self.production_rate - 2)
        else:
            print("Interest received. Adjusting production rate.")
            self.production_rate += 1

        for _ in range(self.production_rate):
            self.send_data(f'/test/data', content='This is data')
