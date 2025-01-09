#SPDX-FileCopyrightText: 2025 Ryosuke Kambara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BatteryStatusListener(Node):
    def __init__(self):
        super().__init__('battery_status_listener')
        self.subscription = self.create_subscription(
            String,
            'battery_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(f'Received message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = BatteryStatusListener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

