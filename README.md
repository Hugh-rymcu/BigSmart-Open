# RYMCU BigSmart 开发板

基于 **ESP32-S3-WROOM-1-N16R8** 的智能语音交互开发板，集成音频系统、显示系统、摄像头、传感器等多种外设。

## 主要特性

- **主控**: ESP32-S3-WROOM-1-N16R8 (16MB Flash + 8MB PSRAM)
- **音频**: ES8311 DAC + ES7210 四通道 ADC + NS4150B 功放
- **显示**: 2.4" ST7789 LCD (320×240) + GT911 电容触摸屏
- **摄像头**: GC0308 (640×480 @ 16fps)
- **传感器**: QMI8658 六轴 (加速度计 + 陀螺仪)
- **存储**: MicroSD 卡槽
- **其他**: WS2812B RGB LED、电池充电管理、按键输入

## 目录结构

```
BigSmart-Open/
├── hardware/
│   ├── mainboard/          # 主板 EDA 工程及原理图
│   └── mics-keys/          # 麦克风按键板 EDA 工程及原理图
├── docs/                   # 硬件配置文档
└── README.md
```

## 硬件文档

详细的硬件配置及引脚分配请参阅 [docs/rymcu-bigsmart-hardware.md](docs/rymcu-bigsmart-hardware.md)。

## 许可证

本项目采用 [Apache-2.0](LICENSE) 许可证开源。
