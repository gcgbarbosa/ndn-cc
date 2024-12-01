import os
from minindn.mininet import MiniNDN
from minindn.node import NDNHost

# Import custom apps
from custom_consumer import CustomConsumer
from custom_intermediate import CustomIntermediate
from custom_producer import CustomProducer

def main():
    # Set up Mini-NDN topology
    topo_file = 'topology.conf'
    os.environ['MININDN_TOPOLOGY_FILE'] = topo_file

    ndn = MiniNDN()
    consumer = ndn.get_node('consumer', cls=NDNHost)
    intermediate = ndn.get_node('intermediate', cls=NDNHost)
    producer = ndn.get_node('producer', cls=NDNHost)

    # Attach custom apps
    consumer.add_application(CustomConsumer)
    intermediate.add_application(CustomIntermediate)
    producer.add_application(CustomProducer)

    # Start the simulation
    ndn.start()

    # Run for 60 seconds
    ndn.run_for(60)

    # Stop the simulation
    ndn.stop()

if __name__ == '__main__':
    main()
