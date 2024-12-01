from minindn.node import NDNForwarder

class CustomIntermediate(NDNForwarder):
    def __init__(self):
        super().__init__()
        self.queue_limit = 10
        self.packet_queue = []

    def on_interest(self, interest):
        if len(self.packet_queue) > self.queue_limit:
            print("Congestion detected. Marking packet with ECN.")
            interest.name += '/ECN'
        self.packet_queue.append(interest)
        self.forward_interest(interest)

    def on_data(self, data):
        self.packet_queue.pop(0)  # Simulate dequeuing
        self.forward_data(data)
