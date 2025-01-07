# mypkg

## 概要
- これはROS2のパッケージで、ロボットシステム学の授業で作成したリポジトリです.

## テスト済みの環境
* Ubuntu 20.04
* Python: 3.7~3.11

## powerwatch.py
バッテリーの残量と状態(充電中/放電中)を現在時刻とともに1秒ごとに公開します

### 実行例
```shell
$ ros2 run mypkg powerwatch
```
バッテリー非接続時
```shell
[INFO] [1735828890.266916584] [powerwatch]: Battery: 83.0%, Status: Discharging, Time: 2025-01-02 23:41:30
```
バッテリー接続時
```shell
[INFO] [1735829670.922016774] [powerwatch]: Battery: 83.5%, Status: Charging, Time: 2025-01-02 23:54:30
```

## LICENSE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。

## Copyright
* © 2024 Ryosuke Kambara

