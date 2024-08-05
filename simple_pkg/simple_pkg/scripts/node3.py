#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class Node3Subscriber(Node):

    def __init__(self):
        super().__init__('node3_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic2',
            self.listener_callback,
            10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info('Received from Node 2: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    node = Node3Subscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
