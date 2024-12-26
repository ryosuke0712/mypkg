import pytest
import rclpy
from std_msgs.msg import Int32
from mypkg.randtalker import RandomNumberTalker

def test_publish_random_number():
    rclpy.init()
    node = RandomNumberTalker()
    received_msg = []

    # サブスクライバでメッセージを受け取るコールバック
    def listener_callback(msg):
        received_msg.append(msg)

    # サブスクライバを作成
    node.create_subscription(Int32, 'random_numbers', listener_callback, 10)

    # ランダムな数をパブリッシュ
    node.publish_random_number()
    rclpy.spin_once(node)

    # メッセージを確認
    assert received_msg
    assert 1 <= received_msg[0].data <= 100

    node.destroy_node()
    rclpy.shutdown()

