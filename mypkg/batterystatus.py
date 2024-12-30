import psutil
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class BatteryStatus(Node):
    def __init__(self):
        super().__init__('batterystatus')
        self.publisher = self.create_publisher(Int32, 'battery_level', 10)
        self.timer = self.create_timer(1.0, self.publish_battery_level)

    def get_battery_percentage(self):
        battery = psutil.sensors_battery()
        if battery is not None:
            return int(battery.percent)  # 整数に変換
        else:
            return 100  # バッテリー情報が取得できない場合、100%として返す

    def publish_battery_level(self):
        battery_level = self.get_battery_percentage()
        msg = Int32()
        msg.data = int(battery_level)  # battery_level を整数に変換
        self.publisher.publish(msg)
        self.get_logger().info(f'Battery level: {battery_level}%')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryStatus()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

