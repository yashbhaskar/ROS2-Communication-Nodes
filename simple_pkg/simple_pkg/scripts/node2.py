#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Node2SubscriberPublisher(Node):

    def __init__(self):
        super().__init__('node2_subscriber_publisher')
        self.subscription = self.create_subscription(
            String,
            'topic1',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'topic2', 10)

    def listener_callback(self, msg):
        self.get_logger().info('Received from Node 1: "%s"' % msg.data)
        new_msg = String()
        new_msg.data = f'Relayed by Node 2: {msg.data}'
        self.publisher_.publish(new_msg)
        self.get_logger().info('Publishing to Node 3: "%s"' % new_msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = Node2SubscriberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
