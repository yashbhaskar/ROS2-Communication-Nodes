# ROS 2 Communication Nodes Project

This project demonstrates a ROS 2 setup with three interconnected nodes designed for multiple communication channels and live information exchange. The nodes are structured to facilitate efficient data flow, real-time processing, and modular development, making them suitable for applications such as image streaming and driver communication in autonomous systems.

## Nodes

### 1. Publisher Node (Node 1)
- **Role**: Publishes messages to a specific topic.
- **Function**: Acts as the initial data source in the communication chain.
- **Applications**: Sending sensor data, status updates, control commands, etc.

### 2. Relay Node (Node 2)
- **Role**: Subscribes to the topic from Node 1, processes or relays the data, and publishes it to a new topic.
- **Function**: Serves as an intermediary between the first and third nodes.
- **Applications**: Data processing, filtering, or transforming information before forwarding it.

### 3. Subscriber Node (Node 3)
- **Role**: Subscribes to the topic from Node 2 and processes the received data.
- **Function**: Receives and handles messages from Node 2.
- **Applications**: Final data handling, decision making, further processing such as visualizations or logging.
