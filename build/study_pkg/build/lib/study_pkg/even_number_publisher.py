#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')
        self.publisher_even = self.create_publisher(Int32, '/even_numbers', 10)
        self.publisher_overflow = self.create_publisher(Int32, '/overflow', 10)
        self.counter = 0
        timer_period = 0.1  # 10 Гц
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_even.publish(msg)
        self.get_logger().info(f'Publishing even: {self.counter}')

        # Проверка на переполнение (>= 100)
        if self.counter >= 100:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.publisher_overflow.publish(overflow_msg)
            self.get_logger().warn(f'Overflow! Published value {self.counter} to /overflow')
            self.counter = 0
        else:
            self.counter += 2

def main(args=None):
    rclpy.init(args=args)
    node = EvenNumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
