import pytest
import rclpy
from std_msgs.msg import Int32
from mypkg.sumlistener import SumListener

def test_sum_listener():
    rclpy.init()
    node = SumListener()
    
    try:
        publisher = node.create_publisher(Int32, 'random_numbers', 10)
        test_data = [10, 20, 30]
        
        # メッセージを送信
        for number in test_data:
            publisher.publish(Int32(data=number))
            rclpy.spin_once(node, timeout_sec=0.1)

        # 合計値を確認
        expected_sum = sum(test_data)
        assert node.total_sum == expected_sum, f"合計値が期待値と異なります: {node.total_sum} != {expected_sum}"

    finally:
        node.destroy_node()
        rclpy.shutdown()

