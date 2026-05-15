# RYMCU BigSmart Firmware Flashing Guide

[中文](README.md) | **English**

This directory stores prebuilt merged firmware images that can be flashed directly to the RYMCU BigSmart development board. The images are organized by firmware source: RYMCU official, Xiaozhi AI official, and Espressif official.

## Firmware Image

| File | Source | Description |
|------|--------|-------------|
| `rymcu-V2.3.19-merged.bin` | RYMCU official | Recommended merged firmware image packaged by RYMCU for BigSmart |
| `xiaozhi-esp32-merged.bin` | Xiaozhi AI official | Merged firmware image for the [78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32) upstream ecosystem |
| `espressif-brookesia-merged.bin` | Espressif official | Merged firmware image for the [espressif/esp-brookesia](https://github.com/espressif/esp-brookesia) upstream ecosystem |

## Before Flashing

- RYMCU BigSmart development board.
- USB Type-C data cable.
- A computer with ESP-IDF, `esptool.py`, or a graphical ESP32 flashing tool installed.
- Confirm the serial port of the board, such as `COM8`.

## Flash with esptool.py

The RYMCU official firmware is recommended as the default. Run this command from the repository root:

```powershell
esptool.py --chip esp32s3 -p COM_PORT -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

For example, if the serial port is `COM8`:

```powershell
esptool.py --chip esp32s3 -p COM8 -b 460800 write_flash 0x0 firmware\rymcu-V2.3.19-merged.bin
```

The merged firmware must be written to Flash offset `0x0`.

To try another official ecosystem, replace the file name in the command with:

```text
firmware\xiaozhi-esp32-merged.bin
firmware\espressif-brookesia-merged.bin
```

## Enter Download Mode

If the flashing tool cannot enter download mode automatically, do it manually:

1. Hold the Boot button.
2. Reset or power-cycle the board.
3. Release the Boot button.
4. Run the flashing command again.

## Check After Flashing

After flashing, the device restarts automatically. In a normal startup:

- The screen turns on and enters the Launcher.
- The home screen shows `rymcu-bigsmart` and the firmware version.
- Serial logs print `RYMCU BigSmart - Starting...`.
- If an SD card is inserted, logs show `SD card mounted at /sdcard`.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Serial port not found | Use a data-capable USB cable and check drivers/device manager |
| Flashing fails | Enter download mode manually, close any serial terminal using the port, and retry |
| No display after flashing | Confirm the image was written at `0x0`, power-cycle the board, and check power |
| Wi-Fi cannot connect | Use 2.4G Wi-Fi and reconfigure the network in Settings |
