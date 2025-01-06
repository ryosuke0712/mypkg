#!/bin/bash
#SPDX-FileCopyrightText: 2025 Ryosuke Kambara
#SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

echo "作業ディレクトリ: $dir/ros2_ws"

cd $dir/ros2_ws || { echo "ディレクトリが見つかりません: $dir/ros2_ws"; exit 1; }

echo "colcon build を実行中..."
colcon build || { echo "colcon build に失敗しました"; exit 1; }

echo "環境設定を読み込み中..."
source $dir/.bashrc || { echo ".bashrc の読み込みに失敗しました"; exit 1; }

echo "talk_listen.launch.py を実行中..."
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log 2>&1 || { 
    echo "launch が失敗またはタイムアウトしました"; 
    cat /tmp/mypkg.log; 
    exit 1; 
}

echo "ログを確認中..."
if grep 'Listen: 10' /tmp/mypkg.log; then
    echo "テスト成功: 'Listen: 10' を検出しました"
else
    echo "テスト失敗: 'Listen: 10' が見つかりませんでした"
    cat /tmp/mypkg.log
    exit 1
fi

