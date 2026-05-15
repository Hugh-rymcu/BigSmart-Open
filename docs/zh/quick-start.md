# RYMCU BigSmart 快速使用指南

[English](../en/quick-start.md)

本指南面向 **RYMCU BigSmart AI助手**，内容根据 `E:\RYMCU\xiaozhi` 工程中的 `main/boards/rymcu-bigsmart` 板级代码整理。它用于帮助用户快速完成开机、联网、语音交互、SD 卡资源准备、视频播放、音乐播放、USB 磁盘模式和 NES 游戏模式。

更完整的编译、烧录和外设说明请参考 [用户详细使用手册](user-manual.md) 与 [硬件配置说明](hardware.md)。

![RYMCU BigSmart 布局图](../../images/layout.png)

## 1. 开发板能力概览

BigSmart 固件目标板卡为 `rymcu-bigsmart`，目标芯片为 `esp32s3`。当前参考工程启用了设备侧 AEC、GC0308 摄像头和 BigSmart 专用外设初始化。

| 模块 | BigSmart 配置 |
|------|---------------|
| 主控 | ESP32-S3-WROOM-1-N16R8 |
| 屏幕 | ST7789，320 x 240，SPI，GT911 触摸 |
| 音频 | ES8311 DAC + ES7210 四通道 ADC + NS4150B 功放 |
| 麦克风 | MIC1 主麦克风，MIC2 副麦克风，MIC3 AEC 参考通道，MIC4 预留 |
| 摄像头 | GC0308，DVP，320 x 240/640 x 480 相关配置，首次使用时懒加载 |
| 存储 | MicroSD，SDMMC 1 线模式，挂载点 `/sdcard` |
| 传感器 | QMI8658 六轴 IMU，支持姿态读取和晃动检测 |
| 灯光 | 1 颗 WS2812B RGB LED，GPIO43 |
| 按键 | Boot 键 GPIO0，GPIO10/PTT 键 |

## 2. 使用前准备

建议准备以下物品：

| 项目 | 用途 |
|------|------|
| RYMCU BigSmart AI助手 | 主设备 |
| USB Type-C 数据线 | 供电、串口日志、固件烧录、USB 磁盘模式 |
| 5V USB 电源或电脑 USB 口 | 供电 |
| MicroSD 卡 | 存放音乐、视频、背景图和 NES ROM |
| 2.4G Wi-Fi | 小智联网、时间同步、网络电台、MQTT 等功能 |
| 蓝牙 HID 手柄 | NES 游戏模式，可选 |

注意事项：

- 请使用可传输数据的 USB 线，只有充电功能的线无法烧录或访问 USB 磁盘模式。
- MicroSD 卡建议格式化为 FAT32。
- ESP32-S3 只支持 2.4G Wi-Fi。
- 固件启动时会优先初始化 SD 卡、屏幕、触摸、Wi-Fi 管理、按键、电池监测、IMU、RGB LED 和 MCP 工具。

## 3. 固件烧录

仓库已提供三份 BigSmart 合并固件：

```text
firmware/rymcu-V2.3.19-merged.bin
firmware/xiaozhi-esp32-merged.bin
firmware/espressif-brookesia-merged.bin
```

默认建议先烧录 RYMCU 官方固件 `rymcu-V2.3.19-merged.bin`。

可使用 ESP-IDF、`esptool.py` 或图形化烧录工具写入 ESP32-S3。命令行示例：

```powershell
esptool.py --chip esp32s3 -p COM端口 -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

例如串口为 `COM8`：

```powershell
esptool.py --chip esp32s3 -p COM8 -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

如果自动进入下载模式失败，可按住 Boot 键后复位或重新上电，再松开 Boot 键重新烧录。

## 4. 开机与首次启动

1. 插入 MicroSD 卡，建议先准备好 `/music`、`/videos`、`/background`、`/nes` 等目录。
2. 使用 USB Type-C 连接电脑或 5V 电源。
3. 长按电源键约 3 秒开机。
4. 屏幕点亮后进入 Launcher 主界面，主界面会显示 `rymcu-bigsmart` 和固件版本。
5. 如需查看日志，使用串口工具连接开发板对应 COM 口。

启动成功时，串口日志中通常可以看到：

```text
RYMCU BigSmart - Starting...
SD card mounted at /sdcard
SD card pins: CLK=47, CMD=48, DAT0=21 (1-line SD mode)
RGB LED strip initialized on GPIO43
WiFi manager initialized early at board startup
```

如果 SD 卡挂载成功，固件会自动检查并创建：

```text
/sdcard/videos
/sdcard/background
```

## 5. 主界面与应用

固件启动后会进入 Launcher。根据 `E:\RYMCU\xiaozhi\main\application.cc`，常见入口包括：

| 应用 | 用途 |
|------|------|
| Xiaozhi | 进入小智语音助手 |
| Settings | 配置 Wi-Fi、服务器、显示等设置 |
| Music | 播放 SD 卡中的 MP3 |
| Radio | 播放网络电台 |
| Video | 播放 `/sdcard/videos` 中的视频资源 |
| Image | 查看图片资源 |
| Camera | 使用 GC0308 摄像头 |
| Gyro | 查看 QMI8658 姿态/传感器能力 |
| Games | 进入游戏相关功能 |
| USB Disk | 重启进入 USB 磁盘模式，将 SD 卡共享给电脑 |

触摸屏可用于点击应用图标、返回、选择文件和调整界面设置。Launcher 的返回按钮由固件统一管理，不同应用中的返回入口可能显示为屏幕按钮。

## 6. Wi-Fi 配网

BigSmart 使用板级 `WifiBoard` 和设置应用完成联网。若没有已保存的 Wi-Fi 配置，固件会在 Launcher 初始化后自动打开 Settings 的网络设置页。

### 6.1 屏幕配网

1. 打开 `Settings`。
2. 进入网络/Wi-Fi 设置页。
3. 扫描附近 Wi-Fi。
4. 选择 2.4G Wi-Fi，输入密码。
5. 保存后等待设备连接。

### 6.2 启动期 Boot 键进入配网

在设备处于启动阶段时，单击 Boot 键会调用板级配网入口，打开 Settings 网络页。

### 6.3 对话中重新配网

BigSmart 注册了 MCP 工具：

```text
self.system.reconfigure_wifi
```

该工具会结束当前对话并进入 Wi-Fi 配置模式。执行前需要用户确认。

### 6.4 热点/蓝牙配网

设置页中还保留了从 Settings 启动 Web 热点配网和 BLE 配网的入口，实际可用性取决于当前固件配置。

## 7. 小智服务器与连接设置

BigSmart 固件会从设置中读取服务器相关配置，例如 OTA URL、MQTT Endpoint、WebSocket URL、客户端 ID、token 等。不同固件版本的界面名称可能不同，通常可在 `Settings` 中完成配置。

常见模式：

| 模式 | 说明 |
|------|------|
| 小智官方 | 使用小智官方服务 |
| RYMCU 官方 | 使用 RYMCU 提供的 BigSmart 配套服务 |
| 自定义 | 填写自建服务地址、MQTT/WebSocket 地址或 token |

修改服务器配置后，建议回到 Launcher 再进入 Xiaozhi，必要时重启设备。

## 8. 按键操作

按键行为来自 `rymcu_bigsmart_board.cc`：

| 操作 | 行为 |
|------|------|
| 电源键长按约 3 秒 | 开机/关机，取决于电源管理电路 |
| Boot 单击 | 启动阶段进入配网；运行时切换小智对话状态 |
| Boot 双击 | 空闲状态切换设备侧 AEC 开/关，需固件启用 `CONFIG_USE_DEVICE_AEC` |
| Boot 长按约 3 秒 | 进入 NES 游戏模式 |
| GPIO10/PTT 按下 | 在空闲或监听状态开始语音监听 |
| GPIO10/PTT 松开 | 在监听状态结束语音监听 |
| 启动时按住 GPIO10 | 进入 USB 磁盘模式 |

GPIO10 在正常运行时是 PTT 按键，在启动检测阶段也用于 USB 磁盘模式入口。

## 9. 语音助手快速使用

1. 确保设备已连接 Wi-Fi。
2. 从 Launcher 打开 `Xiaozhi`。
3. 单击 Boot 键切换对话状态，或按住 GPIO10/PTT 开始说话。
4. 说完后松开 GPIO10/PTT，或等待设备结束监听。
5. 设备通过扬声器播放回复，屏幕显示当前状态。

如果设备播报声容易被再次识别，可在空闲状态双击 Boot 切换设备侧 AEC。

## 10. SD 卡目录

BigSmart SD 卡挂载点为 `/sdcard`，使用 SDMMC 1 线模式：

| 信号 | GPIO |
|------|------|
| CLK | GPIO47 |
| CMD | GPIO48 |
| DAT0 | GPIO21 |

推荐目录：

```text
/sdcard
├── music/          # MP3 音乐，可放子目录
├── videos/         # .mjpg/.mp3/.fps 视频资源
├── background/     # 背景图片资源
└── nes/            # NES ROM
```

固件启动时会自动创建 `/sdcard/videos` 和 `/sdcard/background`。`music` 和 `nes` 目录建议手动创建。

## 11. 音乐播放

`Music` 应用和 MCP 工具都可以播放 SD 卡 MP3。

常用 MCP 工具：

| 功能 | 工具 |
|------|------|
| 播放指定 MP3 | `self.media.play_mp3` |
| 停止播放 | `self.media.stop_mp3` |
| 列出 MP3 文件 | `self.media.list_mp3_files` |
| 查询播放状态 | `self.media.get_mp3_state` |
| 下一首 | `self.media.play_next` |
| 上一首 | `self.media.play_previous` |

示例目录：

```text
/sdcard/music/song1.mp3
/sdcard/music/song2.mp3
```

示例调用：

```json
{
  "tool": "self.media.play_mp3",
  "arguments": {
    "filepath": "/sdcard/music/song1.mp3"
  }
}
```

## 12. 视频播放

`Video` 应用读取固定目录：

```text
/sdcard/videos
```

每个视频需要三个同名文件：

```text
/sdcard/videos/demo.mjpg
/sdcard/videos/demo.mp3
/sdcard/videos/demo.fps
```

| 文件 | 用途 |
|------|------|
| `.mjpg` | 320 x 240 MJPEG 视频流 |
| `.mp3` | 同名音频轨道 |
| `.fps` | 帧率旁路文件，用于音画同步 |

如果 `.fps` 缺失，Video 应用默认按 8 fps 播放。推荐使用仓库中的 [视频转换器](video-converter.md) 生成这三个文件。

推荐参数：

- 分辨率：320 x 240。
- 帧率：8-12 fps。
- JPEG 质量：8。
- MP3：44100 Hz。

操作流程：

1. 在电脑上用 `tools/video-converter/RYMCU-Video-Converter.exe` 转换视频。
2. 将生成的 `.mjpg`、`.mp3`、`.fps` 放入 SD 卡 `/videos` 目录。
3. 开机进入 Launcher。
4. 打开 `Video` 应用。
5. 点击视频条目播放。

## 13. USB 磁盘模式

USB 磁盘模式会把 SD 卡作为 USB 存储设备共享给电脑，适合快速复制音乐、视频、背景图和 ROM。

进入方式：

1. 关机或重启设备。
2. 按住 GPIO10/PTT 键。
3. 上电或复位。
4. 看到 USB Disk Mode 界面后松开按键。
5. 用 USB 数据线连接电脑，SD 卡会显示为 USB 磁盘。

退出方式：

- 在电脑上先安全弹出磁盘。
- 在设备屏幕点击 `Return to Launcher`，或按提示长按 GPIO10 约 1.5 秒退出。

注意：USB 磁盘模式需要插入可正常挂载的 SD 卡。

## 14. NES 游戏模式

BigSmart 集成 NES 模拟器入口，适合配合蓝牙 HID 手柄使用。

准备 ROM：

```text
/sdcard/nes
├── game1.nes
├── game2.nes
└── game3.nes
```

进入游戏：

1. 确保设备处于空闲状态。
2. 长按 Boot 键约 3 秒。
3. 等待进入 NES 游戏菜单。
4. 将蓝牙 HID 手柄进入配对模式。
5. 使用手柄选择 ROM 并开始游戏。

退出或返回：

- 游戏中按 `Start + Select` 返回菜单。
- 菜单中按 `Start + Select` 退出游戏模式。
- `L1 + R1` 长按约 2 秒可重置游戏。

当前固件文档中列出的 Mapper 支持包括 0、1、2、3、4。

## 15. RGB、IMU、MQTT 和摄像头

BigSmart 固件还注册了多种 MCP 工具和本地功能。

### 15.1 RGB LED

```json
{
  "tool": "self.light.set_rgb_color",
  "arguments": {
    "red": 255,
    "green": 100,
    "blue": 50
  }
}
```

关闭：

```json
{
  "tool": "self.light.turn_off",
  "arguments": {}
}
```

### 15.2 IMU 姿态与晃动

QMI8658 会在固件启动后初始化，可用于姿态读取和晃动检测。典型用途包括体感控制、状态触发和互动展示。

### 15.3 智能家居 MQTT

固件包含 SmartHome MQTT 客户端和工具，可配置 broker、连接、发布、订阅、灯控订阅和加湿器示例。常见工具包括：

```text
self.mqtt.configure
self.mqtt.connect
self.mqtt.disconnect
self.mqtt.get_status
self.mqtt.publish
self.mqtt.subscribe
self.mqtt.subscribe_light
self.mqtt.humidifier
```

### 15.4 摄像头

GC0308 摄像头采用懒加载：开机时不立即初始化，首次进入 Camera 应用或首次请求摄像头能力时才初始化。这样可以降低启动阶段的内存压力。

## 16. 常见问题

| 问题 | 排查建议 |
|------|----------|
| 开机屏幕不亮 | 确认长按电源键约 3 秒，检查 USB 供电和数据线 |
| 电脑没有串口 | 换可传输数据的 USB 线，检查驱动和设备管理器 |
| Wi-Fi 扫描不到 | 确认使用 2.4G Wi-Fi，靠近路由器后重试 |
| 无法进入配网 | 启动阶段单击 Boot，或从 Settings 进入网络页 |
| SD 卡挂载失败 | 确认 FAT32 格式，重新插拔或更换 SD 卡 |
| Video 没有文件 | 确认文件放在 `/sdcard/videos`，且至少有 `.mjpg` 文件 |
| 视频有画面无声音 | 确认存在同名 `.mp3` 文件 |
| 视频速度不对 | 确认同名 `.fps` 文件内容是整数帧率 |
| MP3 播放失败 | 确认路径为 `/sdcard/...` 的绝对路径，文件后缀为 `.mp3` |
| USB 磁盘模式进不去 | 启动/复位前按住 GPIO10，并确认插入 SD 卡 |
| NES 找不到游戏 | 确认 `.nes` 文件放在 `/sdcard/nes` |
| 语音识别回声明显 | 空闲状态双击 Boot 切换设备侧 AEC |

## 17. 后续阅读

- [产品介绍书](product-brief.md)
- [用户详细使用手册](user-manual.md)
- [硬件配置说明](hardware.md)
- [视频转换器使用说明](video-converter.md)
