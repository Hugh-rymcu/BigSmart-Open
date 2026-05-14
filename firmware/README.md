# RYMCU BigSmart 固件烧录说明

**中文** | [English](README.en.md)

本目录存放 RYMCU BigSmart 开发板可直接烧录的预编译合并固件。

## 固件文件

| 文件 | 说明 |
|------|------|
| `xiaozhi-V2.3.19-merged.bin` | 适用于 ESP32-S3 的 BigSmart 小智合并固件 |

## 烧录前准备

- RYMCU BigSmart 开发板。
- 可传输数据的 USB Type-C 数据线。
- 已安装 ESP-IDF、`esptool.py` 或图形化 ESP32 烧录工具的电脑。
- 确认开发板串口号，例如 `COM8`。

## 使用 esptool.py 烧录

在仓库根目录执行：

```powershell
esptool.py --chip esp32s3 -p COM端口 -b 460800 write_flash 0x0 firmware\xiaozhi-V2.3.19-merged.bin
```

例如串口为 `COM8`：

```powershell
esptool.py --chip esp32s3 -p COM8 -b 460800 write_flash 0x0 firmware\xiaozhi-V2.3.19-merged.bin
```

合并固件需要写入 Flash 偏移地址 `0x0`。

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
