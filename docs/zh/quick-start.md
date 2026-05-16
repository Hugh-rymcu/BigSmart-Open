



# RYMCU BigSmart 快速使用指南

[English](../en/quick-start.md)

本指南面向 **RYMCU BigSmart AI 助手**，用于帮助用户快速完成开机、联网、语音交互、SD 卡资源准备、音乐播放、视频播放和 USB 磁盘模式等基础操作。

更完整的编译、烧录和外设说明请参考 [用户详细使用手册](user-manual.md) 与 [硬件配置说明](hardware.md)。

<p align="center"><img src="../../images/layout.png" alt="RYMCU BigSmart 布局图" width="800"></p>

## 1. 固件与烧录

BigSmart 出厂已预装 RYMCU 官方固件，可直接开机使用。如需升级或切换固件，请参考仓库中的 [固件烧录说明](../../firmware/README.md)。

仓库提供的固件均为合并固件，使用烧录工具时需要写入 Flash 偏移地址 `0x0`。

## 2. 开机与主界面

### 2.1 开机

1. 长按电源键约 3 秒开机。
2. 如果电池电量不足，请使用 USB Type-C 数据线连接电脑或 5V 电源供电。
3. 屏幕点亮后进入 Home 主界面，界面会显示 `rymcu-bigsmart` 和当前固件版本。
4. 如需查看串口日志，请使用串口工具连接设备对应的 COM 口。

<p align="center"><img src="../../images/home.jpg" alt="BigSmart Home 主界面" width="1536"></p>

### 2.2 主界面与应用

在 Home 主界面左右滑动可切换应用页面。常见应用如下：

| 应用 | 用途 |
|------|------|
| Xiaozhi | 进入小智语音助手 |
| Settings | 配置 Wi-Fi、服务器、显示等设置 |
| Music | 播放 SD 卡中的 MP3 |
| Radio | 播放网络电台 |
| Video | 播放 `/sdcard/videos` 中的视频资源 |
| Image | 查看图片资源 |
| Camera | 使用 GC0308 摄像头 |
| Gyro | 查看 QMI8658 姿态和传感器信息 |
| Games | 进入游戏相关功能 |
| USB Disk | 重启进入 USB 磁盘模式，将 SD 卡共享给电脑 |

触摸屏可用于点击应用图标、返回上级页面、选择文件和调整设置。

<p align="center"><img src="../../images/page1.jpg" alt="BigSmart 应用页面" width="1536"></p>

## 3. Wi-Fi 配网

首次使用时需要先配置 Wi-Fi。BigSmart 支持三种配网方式：屏幕配网、热点网页配网和微信小程序蓝牙配网，任选一种完成即可。

打开 `Settings` 应用，进入 Wi-Fi 设置页。

<p align="center"><img src="../../images/network.png" alt="Wi-Fi 设置入口" width="530"></p>

**注意：BigSmart 仅支持 2.4 GHz Wi-Fi。**

### 3.1 屏幕配网

点击 `Screen WiFi` 进入屏幕配网页面，输入 Wi-Fi 名称和密码后，点击 `Connect` 连接网络。

<p align="center"><img src="../../images/screen.png" alt="屏幕配网页面" width="537"></p>

### 3.2 热点网页配网

点击 `Web Setup` 进入热点配网页面。使用手机连接屏幕上显示的热点，例如 `Xiaozhi-11F0`，手机通常会自动跳转到配网页面；若未自动跳转，可手动打开浏览器访问提示页面并填写 Wi-Fi 信息。

<p align="center"><img src="../../images/hotpot.png" alt="热点网页配网" width="538"></p>

### 3.3 微信小程序蓝牙配网

点击 `BLE Setup` 进入蓝牙配网页面。使用微信扫描屏幕二维码，或在微信中搜索小程序“艾塔达克”。首次使用时请先注册或登录账号。

<p align="center"><img src="../../images/wechat.png" alt="微信小程序蓝牙配网入口" width="532"></p>

小程序操作流程如下：

| 打开小程序 | 选择蓝牙配网 | 完成网络配置 |
|------------|--------------|--------------|
| <img src="../../images/ble1.jpg" alt="微信小程序步骤 1" width="600"> | <img src="../../images/ble2.png" alt="微信小程序步骤 2" width="600"> | <img src="../../images/ble3.png" alt="微信小程序步骤 3" width="600"> |

## 4. 服务商与设备绑定

### 4.1 服务商设置

使用`xiaozhi`语音助手前还需设置服务器地址，通过屏幕配置支持3种服务商配置，如下图所示。

<p align="center"><img src="../../images/advanced.png" alt="高级服务设置" width="527"></p>

其中，`atdak`为`RYMCU`官方服务器，`tenclass`为虾哥小智AI官方服务器，`custom`为自定义服务器，可输入自己的服务器地址。

**设备出场默认使用RYMCU官方服务器。**

### 4.2 设备绑定

首次使用，进入 `Xiaozhi app` 后，设备屏幕会显示激活码或绑定码；在对应小程序或网页后台输入该验证码并确认绑定。

<p align="center"><img src="../../images/peidui.png" alt="设备绑定码" width="531"></p>

**以下3种选择1种即可，出厂默认选择第1种。**

#### 4.2.1 RYMCU官方服务器验证码绑定方法

请登录微信小程序“艾塔达克”，进行绑定如下图所示。

| 设备列表入口 | 输入绑定信息 |
|--------------|--------------|
| <img src="../../images/bd0.png" alt="设备绑定步骤 1" width="600"> | <img src="../../images/bd1.png" alt="设备绑定步骤 2" width="600"> |

#### 4.2.2 虾哥小智AI官方服务器验证码绑定方法

登录官方后台https://xiaozhi.me/console/agents， 先点击“设备管理”，再点击“添加设备”，可在添加设备弹窗中输入设备播报或屏幕显示的 6 位验证码。

<p align="center"><img src="../../images/pd2.png" alt="网页后台添加设备" width="424"></p>

#### 4.2.3 自定义服务器验证码绑定方法

按照自定义服务器进行绑定。

另外，`RYMCU`官方有开源服务器，可以进行自行部署，但需要一定的基础，服务器链接：https://github.com/ruanrongman/IntelliConnect

## 5. 音乐与视频播放

点击屏幕的`Music app`和`Video app`即可播放`SD`卡`mp3`音乐和视频。

| 音乐播放 | 视频播放 |
|----------|----------|
| <img src="../../images/music1.png" alt="音乐播放界面" width="526"> | <img src="../../images/video1.png" alt="视频播放界面" width="537"> |

**需提前将mp3格式音乐和视频文件放入`SD`卡的`music`和`videos`文件夹，操作方法详见下一节。**

视频资源推荐使用仓库中的 [视频转换器](video-converter.md) 生成：

## 6. USB 磁盘模式

USB 磁盘模式会把 SD 卡作为 U盘共享给电脑，适合快速复制音乐、视频、背景图和其他资源。

进入方式：

点击屏幕USB Disk app进入USB转U盘模式，使用USB线连接计算机，计算机即可看到该U盘。

<p align="center"><img src="../../images/u-sd.png" alt="USB 磁盘中的 SD 卡目录" width="378"></p>

**将MP3拷贝到music文件夹即可。**

**常规视频文件需要转换成适合bigsmart AI助手播放的模式，放到videos目录下即可，使用仓库中的 [视频转换器](video-converter.md) 进行转换。**

## 7. 网络电台

点击`radio app`可以播放网络电台。

<p align="center"><img src="../../images/radio.png" alt="网络电台" width="528"></p>

## 8. 游戏

点击`Games app`有多个游戏可玩。

| 游戏列表 | 迷宫游戏 |
|----------|----------|
| <img src="../../images/games.png" alt="游戏列表" width="530"> | <img src="../../images/maze.png" alt="迷宫游戏" width="521"> |

## 9. 扩展能力

BigSmart 固件还注册了多种 MCP 工具和本地功能：

| 能力 | 说明 |
|------|------|
| RGB LED | 支持设置 RGB 颜色和关闭灯光 |
| IMU 姿态与晃动 | QMI8658 可读取姿态数据并支持晃动检测 |
| 智能家居 MQTT | 支持配置 broker、连接、发布、订阅和设备控制示例 |
| 摄像头 | GC0308 采用懒加载方式，首次进入 Camera 或请求摄像头能力时初始化 |

## 10. 常见问题

| 问题 | 排查建议 |
|------|----------|
| 开机屏幕不亮 | 确认长按电源键约 3 秒，检查电池电量、USB 供电和数据线 |
| 电脑没有串口 | 更换可传输数据的 USB 线，检查驱动和设备管理器 |
| Wi-Fi 扫描不到 | 确认使用 2.4 GHz Wi-Fi，靠近路由器后重试 |
| 无法进入配网 | 从 `Settings` 进入 Wi-Fi 页面，或重启后重新进入配网流程 |
| SD 卡挂载失败 | 确认 FAT32 格式，重新插拔或更换 SD 卡 |
| Video 没有文件 | 确认文件放在 `/sdcard/videos`，且至少有 `.mjpg` 文件 |
| 视频有画面无声音 | 确认存在同名 `.mp3` 文件 |
| 视频速度不对 | 确认同名 `.fps` 文件内容是整数帧率 |
| MP3 播放失败 | 确认路径为 `/sdcard/...` 的绝对路径，文件后缀为 `.mp3` |
| USB 磁盘模式进不去 | 启动或复位前按住 GPIO10，并确认插入 SD 卡 |
| 语音识别回声明显 | 空闲状态双击 Boot 切换设备侧 AEC |

## 11. 后续阅读

- [产品介绍书](product-brief.md)
- [用户详细使用手册](user-manual.md)
- [硬件配置说明](hardware.md)
- [视频转换器使用说明](video-converter.md)
