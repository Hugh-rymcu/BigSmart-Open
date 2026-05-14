# RYMCU BigSmart Development Board

[中文](README.md) | **English**

RYMCU BigSmart is an ESP32-S3 smart voice interaction development board based on **ESP32-S3-WROOM-1-N16R8**. It integrates audio, display, camera, motion sensing, MicroSD storage, battery power management, and physical controls in one compact open hardware platform.

## Key Features

- **MCU**: ESP32-S3-WROOM-1-N16R8 (16 MB Flash + 8 MB PSRAM)
- **Audio**: ES8311 DAC + ES7210 four-channel ADC + NS4150B power amplifier
- **Display**: 2.4" ST7789 LCD (320 x 240) + GT911 capacitive touch panel
- **Camera**: GC0308 (640 x 480 @ 16 FPS)
- **Sensor**: QMI8658 six-axis accelerometer/gyroscope
- **Storage**: MicroSD card slot
- **Other**: WS2812B RGB LED, battery charging management, button input

## Repository Layout

```text
BigSmart-Open/
├── hardware/
│   ├── mainboard/          # Mainboard EDA project and schematics
│   └── mics-keys/          # Microphone/button board EDA project and schematics
├── enclosure/              # Fusion 360 enclosure design files
├── docs/
│   ├── zh/                 # Chinese documentation
│   └── en/                 # English documentation
├── firmware/               # Prebuilt merged firmware images
├── tools/
│   └── video-converter/    # BigSmart video converter
└── README.md
```

## Documentation

| English | 中文 |
|---------|------|
| [Quick Start Guide](docs/en/quick-start.md) | [快速使用指南](docs/zh/quick-start.md) |
| [Product Brief](docs/en/product-brief.md) | [产品介绍书](docs/zh/product-brief.md) |
| [User Manual](docs/en/user-manual.md) | [用户详细使用手册](docs/zh/user-manual.md) |
| [Hardware Configuration](docs/en/hardware.md) | [硬件配置说明](docs/zh/hardware.md) |
| [Video Converter User Guide](docs/en/video-converter.md) | [视频转换器使用说明](docs/zh/video-converter.md) |

## Firmware

- [xiaozhi-V2.3.19-merged.bin](firmware/xiaozhi-V2.3.19-merged.bin)
- [Firmware flashing guide](firmware/README.en.md)

## License

- **Personal DIY / non-commercial use**: licensed under [Apache-2.0](LICENSE).
- **Commercial use**: requires commercial authorization from RYMCU. Contact [RYMCU](mailto:hugh@rymcu.com) for licensing details.
