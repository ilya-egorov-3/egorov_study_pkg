#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class OverflowListener(Node):
    def __init__(self):
        super().__init__('overflow_listener')

        # Параметр – имя топика для прослушивания
        self.declare_parameter('topic_name', '/overflow')
        topic = self.get_parameter('topic_name').get_parameter_value().string_value

        self.subscription = self.create_subscription(
            Int32,
            topic,
            self.listener_callback,
            10
        )
        self.get_logger().info(f'Listener subscribed to {topic}')

    def listener_callback(self, msg):
        self.get_logger().warn(f'!!! ПЕРЕПОЛНЕНИЕ !!! Получено значение: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OverflowListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
