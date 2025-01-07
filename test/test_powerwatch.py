#SPDX-FileCopyrightText: 2025 Ryosuke Kambara
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from std_msgs.msg import String
from mypkg.powerwatch import PowerWatch

def test_publish_battery_status():
    rclpy.init()
    node = PowerWatch()
    received_msg = None

    def listener_callback(msg):
        nonlocal received_msg
        received_msg = msg.data

    node.create_subscription(String, 'battery_status', listener_callback, 10)

    node.publish_battery_status()
    rclpy.spin_once(node)

    node.destroy_node()
    rclpy.shutdown()
