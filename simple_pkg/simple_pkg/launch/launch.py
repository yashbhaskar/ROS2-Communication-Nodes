from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='simple_pkg',
            executable='node1.py',
            name='NodePub'
        ),
        Node(
            package='simple_pkg',
            executable='node2.py',
            name='NodePubSub'
        ),
        Node(
            package='simple_pkg',
            executable='node2.py',
            name='NodeSub'
        )
    ])
