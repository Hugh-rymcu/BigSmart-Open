# RYMCU BigSmart Firmware Flashing Guide

[中文](README.md) | **English**

This directory stores prebuilt merged firmware images that can be flashed directly to the RYMCU BigSmart development board.

## Firmware Image

| File | Description |
|------|-------------|
| `xiaozhi-V2.3.19-merged.bin` | BigSmart Xiaozhi merged firmware image for ESP32-S3 |

## Before Flashing

- RYMCU BigSmart development board.
- USB Type-C data cable.
- A computer with ESP-IDF, `esptool.py`, or a graphical ESP32 flashing tool installed.
- Confirm the serial port of the board, such as `COM8`.

## Flash with esptool.py

Run this command from the repository root:

```powershell
esptool.py --chip esp32s3 -p COM_PORT -b 460800 write_flash 0x0 firmware\xiaozhi-V2.3.19-merged.bin
```

For example, if the serial port is `COM8`:

```powershell
esptool.py --chip esp32s3 -p COM8 -b 460800 write_flash 0x0 firmware\xiaozhi-V2.3.19-merged.bin
```

The merged firmware must be written to Flash offset `0x0`.

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
