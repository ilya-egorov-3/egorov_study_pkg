#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from datetime import datetime

class TimePrinter(Node):
    def __init__(self):
        super().__init__('time_printer')
        self.create_timer(5.0, self.timer_callback)
        self.get_logger().info('Узел запущен')

    def timer_callback(self, timer=None):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.get_logger().info(f'Текущее время: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()
