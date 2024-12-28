# ros2

## 概要
- ロボットシステム学の授業で作成したリポジトリです

## テスト済みの環境
* Ubuntu 20.04
* Python: 3.7~3.11

## 使用準備
### リポジトリを適当な場所にクローンしてください
```shell
$ git clone https://github.com/ryosuke0712/ros2.git
```

### ros2_wsに移動してください
```shell
$ cd ~/ros2_ws
```

## randtalker.py
0.5秒ごとにランダムな整数(1から100の範囲)を生成し,random_numbersトピックにInt32型メッセージとして送信し,送信された整数をログとして表示します。

### 使用例
```shell
$ ros2 run mypkg randtalker
```
[INFO] [randtalker]: Publishing (randtalker): 42

[INFO] [randtalker]: Publishing (randtalker): 17

