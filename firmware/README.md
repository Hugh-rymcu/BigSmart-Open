# Firmware

This directory stores prebuilt firmware images for the RYMCU BigSmart development board.

## Available Images

| File | Description |
|------|-------------|
| `xiaozhi-V2.3.19-merged.bin` | Xiaozhi BigSmart merged firmware image for ESP32-S3 |

## Flashing

Use ESP-IDF, `esptool.py`, or a GUI flashing tool to write the merged image at flash offset `0x0`.

Example:

```powershell
esptool.py --chip esp32s3 -p COM_PORT -b 460800 write_flash 0x0 firmware\xiaozhi-V2.3.19-merged.bin
```

Replace `COM_PORT` with the serial port of your device, such as `COM8`.
