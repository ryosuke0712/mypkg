#!/bin/bash

dir=~  # デフォルトのディレクトリ
[ "$1" != "" ] && dir="$1"  # 引数があればそれを使用

echo "作業ディレクトリ: $dir/ros2_ws"

# ディレクトリに移動できなければ終了
cd $dir/ros2_ws || { echo "ディレクトリが見つかりません: $dir/ros2_ws"; exit 1; }

# colcon build を実行
echo "colcon build を実行中..."
colcon build || { echo "colcon build に失敗しました"; exit 1; }

# 環境を設定
echo "環境設定を読み込み中..."
source $dir/.bashrc || { echo ".bashrc の読み込みに失敗しました"; exit 1; }

# ROS 2のlaunchファイルを実行
echo "talk_listen.launch.py を実行中..."
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || { 
    echo "launch が失敗またはタイムアウトしました"; 
    cat /tmp/mypkg.log; 
    exit 1; 
}

# ログを確認
echo "ログを確認中..."
if grep 'Listen: 10' /tmp/mypkg.log; then
    echo "テスト成功: 'Listen: 10' を検出しました"
else
    echo "テスト失敗: 'Listen: 10' が見つかりませんでした"
    cat /tmp/mypkg.log
    exit 1
fi

