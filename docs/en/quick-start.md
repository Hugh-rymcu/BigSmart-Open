# RYMCU BigSmart Quick Start Guide

[中文](../zh/quick-start.md)

This guide is written for the **RYMCU BigSmart AI assistant**. It helps users complete first boot, network setup, voice interaction, SD card resource preparation, music playback, video playback, and USB disk mode.

For complete build, flashing, and hardware details, see the [User Manual](user-manual.md) and [Hardware Configuration](hardware.md).

<p align="center"><img src="../../images/layout-en.png" alt="RYMCU BigSmart layout" width="800"></p>

## 1. Firmware and Flashing

BigSmart ships with the RYMCU official firmware preinstalled and can be used directly after power-on. To upgrade or switch firmware, see the [firmware flashing guide](../../firmware/README.en.md).

The firmware images in this repository are merged images. When using a flashing tool, write the image to Flash offset `0x0`.

## 2. Power On and Home Screen

### 2.1 Power On

1. Hold the power button for about 3 seconds.
2. If the battery is low, connect the board to a computer or 5 V power supply with a USB Type-C data cable.
3. After the screen turns on, the Home screen appears and shows `rymcu-bigsmart` and the current firmware version.
4. To view logs, connect to the corresponding COM port with a serial terminal.

<p align="center"><img src="../../images/home.jpg" alt="BigSmart Home screen" width="1536"></p>

### 2.2 Home Screen and Apps

Swipe left or right on the Home screen to switch app pages. Common apps include:

| App | Purpose |
|-----|---------|
| Xiaozhi | Start the Xiaozhi voice assistant |
| Settings | Configure Wi-Fi, server, display, and other settings |
| Music | Play MP3 files from the SD card |
| Radio | Play internet radio |
| Video | Play video resources from `/sdcard/videos` |
| Image | View image resources |
| Camera | Use the GC0308 camera |
| Gyro | View QMI8658 attitude and sensor information |
| Games | Enter game-related features |
| USB Disk | Reboot into USB disk mode and share the SD card with a PC |

Use the touch screen to open apps, go back, select files, and adjust settings.

<p align="center"><img src="../../images/page1.jpg" alt="BigSmart app page" width="1536"></p>

## 3. Wi-Fi Setup

Wi-Fi must be configured before first use. BigSmart supports three provisioning methods: on-screen setup, hotspot web setup, and WeChat mini program BLE setup. Choose any one of them.

Open the `Settings` app and enter the Wi-Fi settings page.

<p align="center"><img src="../../images/network.png" alt="Wi-Fi settings entry" width="530"></p>

Note: BigSmart supports 2.4 GHz Wi-Fi only.

### 3.1 On-screen Wi-Fi Setup

Tap `Screen WiFi`, enter the Wi-Fi SSID and password, and tap `Connect`.

<p align="center"><img src="../../images/screen.png" alt="On-screen Wi-Fi setup" width="537"></p>

### 3.2 Hotspot Web Setup

Tap `Web Setup` to open hotspot provisioning. Connect your phone to the hotspot shown on the screen, such as `Xiaozhi-11F0`. The phone usually opens the setup page automatically; if not, open the browser page shown by the device and enter the Wi-Fi information manually.

<p align="center"><img src="../../images/hotpot.png" alt="Hotspot web setup" width="538"></p>

### 3.3 WeChat Mini Program BLE Setup

Tap `BLE Setup` to open BLE provisioning. Scan the QR code on the device with WeChat, or search for the mini program `艾塔达克`. Register or sign in before provisioning if prompted.

<p align="center"><img src="../../images/wechat.png" alt="WeChat mini program BLE entry" width="532"></p>

Mini program flow:

| Open the mini program | Select BLE setup | Complete Wi-Fi setup |
|-----------------------|------------------|----------------------|
| <img src="../../images/ble1.jpg" alt="WeChat mini program step 1" width="600"> | <img src="../../images/ble2.png" alt="WeChat mini program step 2" width="600"> | <img src="../../images/ble3.png" alt="WeChat mini program step 3" width="600"> |

## 4. Service Provider and Device Binding

### 4.1 Service Provider Settings

BigSmart reads server settings such as OTA URL, MQTT endpoint, WebSocket URL, client ID, and token from stored settings. Names may differ between firmware versions, but they are usually configured in `Settings`.

Common modes:

| Mode | Description |
|------|-------------|
| Xiaozhi official | Use the official Xiaozhi service |
| RYMCU official | Use the RYMCU service adapted for BigSmart |
| Custom | Enter a self-hosted service, MQTT/WebSocket URL, or token |

After changing server settings, return to the Home screen and reopen Xiaozhi. Reboot the device if needed.

<p align="center"><img src="../../images/advanced.png" alt="Advanced service settings" width="527"></p>

### 4.2 Device Binding

Some services require device binding. After entering Xiaozhi, the device shows an activation or binding code. Enter that code in the corresponding mini program or web console and confirm the binding.

<p align="center"><img src="../../images/peidui.png" alt="Device binding code" width="531"></p>

#### 4.2.1 RYMCU Official Server Verification-Code Binding

Log in to the WeChat mini program "艾塔达克" and bind the device as shown below.

| Device list entry | Enter binding information |
|-------------------|---------------------------|
| <img src="../../images/bd0.png" alt="Device binding step 1" width="600"> | <img src="../../images/bd1.png" alt="Device binding step 2" width="600"> |

#### 4.2.2 Xiaoge Xiaozhi AI Official Server Verification-Code Binding

Log in to the official console at https://xiaozhi.me/console/agents, click "Device Management", then click "Add Device". Enter the 6-digit verification code spoken by the device or shown on the screen in the add-device dialog.

<p align="center"><img src="../../images/pd2.png" alt="Web console add-device dialog" width="424"></p>

## 5. SD Card and Media Resources

### 5.1 SD Card Layout

BigSmart mounts the SD card at `/sdcard` using SDMMC 1-line mode. Format the MicroSD card as FAT32 and organize resources as follows:

```text
/sdcard
├── music/          # MP3 music, subdirectories allowed
├── videos/         # .mjpg/.mp3/.fps video resources
├── background/     # Background images
└── photos/         # Image resources, optional
```

The firmware automatically creates `/sdcard/videos` and `/sdcard/background` on startup. Create `music`, `photos`, and other resource directories manually as needed.

<p align="center"><img src="../../images/u-sd.png" alt="SD card folders in USB disk mode" width="378"></p>

### 5.2 Music and Video Playback

The `Music` app plays MP3 files from the SD card. The `Video` app reads video resources from `/sdcard/videos`.

| Music playback | Video playback |
|----------------|----------------|
| <img src="../../images/music1.png" alt="Music playback screen" width="526"> | <img src="../../images/video1.png" alt="Video playback screen" width="537"> |

Example music directory:

```text
/sdcard/music/song1.mp3
/sdcard/music/song2.mp3
```

Each video should use three files with the same base name:

```text
/sdcard/videos/demo.mjpg
/sdcard/videos/demo.mp3
/sdcard/videos/demo.fps
```

| File | Purpose |
|------|---------|
| `.mjpg` | 320 x 240 MJPEG video stream |
| `.mp3` | Matching audio track |
| `.fps` | Frame-rate sidecar for audio/video sync |

If `.fps` is missing, the Video app falls back to 8 fps.

Use the repository [Video Converter](video-converter.md) to generate video resources:

- Resolution: 320 x 240.
- Frame rate: 8-12 fps.
- JPEG quality: 8.
- MP3: 44100 Hz.

## 6. USB Disk Mode

USB disk mode shares the SD card with a PC as a USB storage device. It is useful for copying music, videos, background images, and other resources.

Enter USB disk mode:

1. Power off or restart the device.
2. Hold GPIO10/PTT.
3. Power on or reset.
4. Release the button after the USB Disk Mode screen appears.
5. Connect the USB data cable to the PC. The SD card appears as a USB drive.

Exit:

- Safely eject the drive on the PC first.
- Tap `Return to Launcher` on the device, or hold GPIO10 for about 1.5 seconds as prompted.

Note: USB disk mode requires a mounted SD card.

## 7. Extended Features

BigSmart firmware also registers local features and MCP tools:

| Feature | Description |
|---------|-------------|
| RGB LED | Set RGB colors and turn the light off |
| IMU attitude and shake | QMI8658 reads attitude data and supports shake detection |
| Smart home MQTT | Configure broker, connect, publish, subscribe, and control example devices |
| Camera | GC0308 is lazily initialized when opening Camera or requesting camera capability for the first time |

## 8. Troubleshooting

| Problem | Suggestion |
|---------|------------|
| Screen does not turn on | Hold the power button for about 3 seconds; check battery level, USB power, and cable |
| No serial port on PC | Use a data-capable USB cable and check drivers/device manager |
| Wi-Fi not found | Use 2.4 GHz Wi-Fi and retry near the router |
| Cannot enter Wi-Fi setup | Open the Wi-Fi page from `Settings`, or reboot and restart the provisioning flow |
| SD card mount fails | Use FAT32, reinsert the card, or try another card |
| Video app shows no files | Put files under `/sdcard/videos`; at least a `.mjpg` file is required |
| Video has no sound | Make sure a same-name `.mp3` file exists |
| Video speed is wrong | Make sure the same-name `.fps` file contains an integer frame rate |
| MP3 playback fails | Use an absolute `/sdcard/...` path and confirm the `.mp3` extension |
| USB disk mode does not enter | Hold GPIO10 before startup/reset and make sure an SD card is inserted |
| Voice recognition has echo | Double-click Boot while idle to toggle device-side AEC |

## 9. Next Reading

- [Product Brief](product-brief.md)
- [User Manual](user-manual.md)
- [Hardware Configuration](hardware.md)
- [Video Converter User Guide](video-converter.md)
