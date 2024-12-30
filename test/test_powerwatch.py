import pytest
import rclpy
from std_msgs.msg import String
from mypkg.powerwatch import PowerWatch

def test_publish_battery_status():
    rclpy.init()
    node = PowerWatch()
    received_msg = []

    def listener_callback(msg):
        received_msg.append(msg)

    node.create_subscription(String, 'battery_status', listener_callback, 10)

    node.publish_battery_status()
    rclpy.spin_once(node)

    # メッセージを確認
    assert received_msg
    assert isinstance(received_msg[0].data, str)
    assert "Battery:" in received_msg[0].data
    assert "Status:" in received_msg[0].data
    assert "Time:" in received_msg[0].data

    node.destroy_node()
    rclpy.shutdown()

