import psutil
from datetime import datetime
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PowerWatch(Node):
    def __init__(self):
        super().__init__('powerwatch')
        self.publisher = self.create_publisher(String, 'battery_status', 10)
        self.timer = self.create_timer(1.0, self.publish_battery_status)

    def get_battery_status(self):
        battery = psutil.sensors_battery()
        if battery:
            battery_level = battery.percent  # バッテリー残量（%）
            charging_status = "Charging" if battery.power_plugged else "Discharging"
            return battery_level, charging_status
        else:
            return None, "No battery information available"

    def publish_battery_status(self):
        battery_level, charging_status = self.get_battery_status()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 現在時刻
        if battery_level is not None:
            message = (
                f"Battery: {battery_level:.1f}%, Status: {charging_status}, Time: {current_time}"
            )
        else:
            message = f"{charging_status}, Time: {current_time}"

        msg = String()
        msg.data = message
        self.publisher.publish(msg)
        self.get_logger().info(message)


def main(args=None):
    rclpy.init(args=args)
    node = PowerWatch()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

