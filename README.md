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
├── enclosure/              # 外壳 3D 设计文件 (Fusion 360)
├── docs/                   # 硬件配置文档
└── README.md
```

## 文档

- [产品介绍书](docs/rymcu-bigsmart-product-brief.md)
- [用户详细使用手册](docs/rymcu-bigsmart-user-manual.md)
- [硬件配置说明](docs/rymcu-bigsmart-hardware.md)

## 许可证

- **个人 DIY / 非商业用途**：遵循 [Apache-2.0](LICENSE) 开源许可证。
- **商业用途**：需取得 RYMCU 商用授权，请联系 [RYMCU 官方](mailto:hugh@rymcu.com) 获取授权详情。
