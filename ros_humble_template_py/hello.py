import rclpy
from rclpy.node import Node

class Hello(Node):
    def __init__(self):
        super().__init__('hello')
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info('Hello World')

def main(args=None):
    rclpy.init(args=args)
    hello = Hello()
    rclpy.spin(hello)
    hello.destroy_node()
    rclpy.shutdown()
