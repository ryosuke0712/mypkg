import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import random

class RandomNumberTalker(Node):
    def __init__(self):
        super().__init__('random_number_talker')
        self.publisher_ = self.create_publisher(Int32, 'random_numbers', 10)
        self.timer = self.create_timer(0.5, self.publish_random_number)

    def publish_random_number(self):
        number = random.randint(1, 100)
        msg = Int32()
        msg.data = number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing (randtalker): {number}')

def main(args=None):
    rclpy.init(args=args)
    node = RandomNumberTalker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

