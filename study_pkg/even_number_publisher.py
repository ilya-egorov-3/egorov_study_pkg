#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberPublisher(Node):
    def __init__(self):
        super().__init__('even_pub')

        # Объявляем параметры с значениями по умолчанию
        self.declare_parameter('frequency', 1.0)               # Гц
        self.declare_parameter('overflow_threshold', 100)      # порог переполнения
        self.declare_parameter('topic_name', '/even_numbers')  # топик для чётных чисел

        # Получаем значения параметров
        freq = self.get_parameter('frequency').get_parameter_value().double_value
        threshold = self.get_parameter('overflow_threshold').get_parameter_value().integer_value
        topic = self.get_parameter('topic_name').get_parameter_value().string_value

        # Создаём публикаторы
        self.publisher_even = self.create_publisher(Int32, topic, 10)
        self.publisher_overflow = self.create_publisher(Int32, '/overflow', 10)

        self.counter = 0
        self.threshold = threshold

        # Таймер с динамической частотой
        self.timer = self.create_timer(1.0 / freq, self.timer_callback)

        self.get_logger().info(
            f'Publisher started: freq={freq} Hz, threshold={threshold}, topic={topic}'
        )

    def timer_callback(self):
        msg = Int32()
        msg.data = self.counter
        self.publisher_even.publish(msg)
        self.get_logger().info(f'Publishing even: {self.counter}')

        # Проверка на переполнение (>= порога)
        if self.counter >= self.threshold:
            overflow_msg = Int32()
            overflow_msg.data = self.counter
            self.publisher_overflow.publish(overflow_msg)
            self.get_logger().warn(f'Overflow! Published {self.counter} to /overflow')
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
