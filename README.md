# mypkg

## 概要
- これはROS2のパッケージで、ロボットシステム学の授業で作成したリポジトリです。
- バッテリーの残量と状態をbattery_statusトピックにパブリッシュします。
- talk_listen.launch.pyはテスト用です。

## ノード
- powerwatch:
  バッテリーの残量と状態(充電中/放電中)を現在時刻とともに1秒ごとに公開します.

## テスト済みの環境
### テスト環境
* Ubuntu 22.04
* ROS2 Humble

### 開発環境
* Ubuntu 20.04
* ROS2 Foxy

## 使用方法
このコマンドで実行します。
```shell
$ ros2 run mypkg powerwatch
```

トピック内容はこのコマンドで確認できます。
```shell
$ ros2 topic echo battery_status
```
```shell
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:30'
---
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:31'
---
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:32'
---
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:33'
---
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:34'
---
data: 'Battery: 61.5%, Status: Discharging, Time: 2025-01-07 23:34:35'
---
```

## LICENSE
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます。

## Copyright
* © 2025 Ryosuke Kambara

