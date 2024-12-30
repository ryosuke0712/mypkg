import pytest
import rclpy
from std_msgs.msg import Int32
from mypkg.batterystatus import BatteryStatus

def test_publish_battery_level():
    rclpy.init()
    node = BatteryStatus()
    received_msg = []

    # サブスクライバでメッセージを受け取るコールバック
    def listener_callback(msg):
        received_msg.append(msg)

    # サブスクライバを作成
    node.create_subscription(Int32, 'battery_level', listener_callback, 10)

    # バッテリー状態をパブリッシュ
    node.publish_battery_level()
    rclpy.spin_once(node)

    # メッセージを確認
    assert received_msg
    assert isinstance(received_msg[0].data, int)
    assert 0 <= received_msg[0].data <= 100

    node.destroy_node()
    rclpy.shutdown()

