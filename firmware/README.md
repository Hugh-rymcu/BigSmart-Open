# RYMCU BigSmart 固件烧录说明

**中文** | [English](README.en.md)

本目录存放 RYMCU BigSmart AI助手可直接烧录的预编译合并固件，按固件来源分为 RYMCU 官方、小智 AI 官方和乐鑫科技官方三个版本。

## 固件文件

| 文件 | 来源 | 说明 |
|------|------|------|
| `rymcu-V2.3.19-merged.bin` | RYMCU 官方 | RYMCU 针对 BigSmart 整理发布的推荐合并固件 |
| `xiaozhi-esp32-merged.bin` | 小智 AI 官方 | 对应 [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) 主线生态的合并固件 |
| `espressif-brookesia-merged.bin` | 乐鑫科技官方 | 对应 [espressif/esp-brookesia](https://github.com/espressif/esp-brookesia) 主线生态的合并固件 |

## 烧录前准备

- RYMCU BigSmart AI助手。
- 可传输数据的 USB Type-C 数据线。
- 已安装 ESP-IDF、`esptool.py` 或图形化 ESP32 烧录工具的电脑。
- 确认开发板串口号，例如 `COM8`。

## 使用 esptool.py 烧录

默认建议先烧录 RYMCU 官方固件。在仓库根目录执行：

```powershell
esptool.py --chip esp32s3 -p COM端口 -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

例如串口为 `COM8`：

```powershell
esptool.py --chip esp32s3 -p COM8 -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

合并固件需要写入 Flash 偏移地址 `0x0`。

如需体验其他官方生态，可将命令中的文件名替换为：

```text
firmware\xiaozhi-esp32-merged.bin
firmware\espressif-brookesia-merged.bin
```

## 进入下载模式

如果烧录工具无法自动进入下载模式，可手动操作：

1. 按住 Boot 键。
2. 复位或重新上电。
3. 松开 Boot 键。
4. 重新执行烧录命令。

## 烧录后检查

烧录完成后设备会自动重启。正常情况下可以看到：

- 屏幕亮起并进入 Launcher。
- 主界面显示 `rymcu-bigsmart` 和固件版本。
- 串口日志打印 `RYMCU BigSmart - Starting...`。
- 若已插入 SD 卡，日志显示 `SD card mounted at /sdcard`。

## 常见问题

| 问题 | 处理方法 |
|------|----------|
| 找不到串口 | 更换可传输数据的 USB 线，检查驱动和设备管理器 |
| 烧录失败 | 手动进入下载模式，关闭占用串口的串口终端后重试 |
| 烧录后无显示 | 确认固件写入地址为 `0x0`，重新上电，检查供电 |
| Wi-Fi 无法连接 | 使用 2.4G Wi-Fi，在 Settings 中重新配网 |
