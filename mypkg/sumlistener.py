import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SumListener(Node):
    def __init__(self):
        super().__init__('sum_listener')
        self.subscription = self.create_subscription(
            Int32,
            'random_numbers',  # 発行されるトピック名
            self.listener_callback,
            10
        )
        self.total_sum = 0

    def listener_callback(self, msg):
        self.total_sum += msg.data
        self.get_logger().info(f'Received: {msg.data}, Total Sum: {self.total_sum}')

def main(args=None):
    rclpy.init(args=args)
    node = SumListener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

