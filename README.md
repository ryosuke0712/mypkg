# ros2

## 概要
- ロボットシステム学の授業で作成したリポジトリです.

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
[INFO] [randtalker]: Publishing (randtalker): 42
[INFO] [randtalker]: Publishing (randtalker): 17
```

## sumlistener.py
random_numbersトピックからメッセージを受信し、受け取った数値を合計していきます。

### 使用例
```shell
$ ros2 run mypkg sumlistener
[INFO] [sumlistener]: Received: 42, Running Total: 42
[INFO] [sumlistener]: Received: 17, Running Total: 59
```

## LICENSE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。

## Copyright
* © 2024 Ryosuke Kambara

