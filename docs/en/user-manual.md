# RYMCU BigSmart User Manual

[中文](../zh/user-manual.md)

## 1. Before You Start

### 1.1 Required Items

| Item | Purpose |
|------|---------|
| RYMCU BigSmart development board | Main device |
| USB Type-C data cable | Power, serial logs, firmware flashing |
| 5 V USB power supply or computer USB port | Power |
| MicroSD card | Stores MP3, NES ROM, video, and other resources |
| Bluetooth HID gamepad | Optional NES game controller |
| 2.4G Wi-Fi network | Xiaozhi, internet radio, MQTT, and other connected features |

### 1.2 Notes

- Use a USB cable that supports data transfer. Charge-only cables cannot flash firmware or show serial logs.
- Format the MicroSD card as FAT32.
- ESP32-S3 supports 2.4G Wi-Fi only. Do not use a 5G-only network.
- Camera, audio, display, and Wi-Fi features all consume memory. During development, verify basic features first, then enable advanced features one by one.
- This manual uses the BigSmart Xiaozhi firmware under `E:\RYMCU\xiaozhi` as the software reference. If you use other firmware, button behavior and menu flow may differ.

## 2. Development Environment

### 2.1 Recommended Environment

| Tool | Recommended version / note |
|------|----------------------------|
| ESP-IDF | 5.4 or later |
| IDE | VSCode, Cursor, or command line |
| Serial terminal | ESP-IDF Monitor, PuTTY, MobaXterm, or another serial terminal |
| Firmware project | `E:\RYMCU\xiaozhi` |
| Hardware repository | `E:\RYMCU\BigSmart-Open` |

### 2.2 Project Locations

Hardware open files are in this repository:

```text
E:\RYMCU\BigSmart-Open
```

The Xiaozhi firmware reference project is located at:

```text
E:\RYMCU\xiaozhi
```

## 3. Firmware Build and Flashing

### 3.1 Build with ESP-IDF

Enter the Xiaozhi firmware project:

```powershell
cd E:\RYMCU\xiaozhi
idf.py set-target esp32s3
idf.py build
```

### 3.2 Flash Firmware

Connect BigSmart to the computer through USB, confirm the serial port, then run:

```powershell
idf.py -p COM_PORT flash monitor
```

Example:

```powershell
idf.py -p COM8 flash monitor
```

### 3.3 Flash a Merged Firmware Image

The Xiaozhi project provides a merged firmware image example:

```text
E:\RYMCU\xiaozhi\bin\xiaozhi-V2.3.5-merged.bin
```

You can flash it with ESP-IDF, `esptool.py`, or a GUI flashing tool. A common command-line method is:

```powershell
esptool.py --chip esp32s3 -p COM_PORT -b 460800 write_flash 0x0 bin\xiaozhi-V2.3.5-merged.bin
```

### 3.4 Enter Download Mode

If automatic flashing fails, enter download mode manually:

1. Hold the Boot button.
2. Reset or power-cycle the board.
3. Release the Boot button.
4. Run the flashing command again.

## 4. First Boot and Wi-Fi Provisioning

### 4.1 Startup Check

After flashing, the device restarts. In a normal startup:

- The screen turns on and shows the Xiaozhi UI.
- Serial logs print board initialization information.
- If an SD card is present, logs show it mounted at `/sdcard`.
- If Wi-Fi is not configured, the device enters provisioning.

### 4.2 Wi-Fi Provisioning

The Xiaozhi reference project includes BluFi provisioning documentation. A typical flow:

1. Enable `WiFi Configuration Method -> Esp Blufi` during build configuration.
2. On first boot without saved Wi-Fi credentials, the device enters provisioning automatically.
3. Use the EspBlufi app or another compatible BluFi client to find the device.
4. Connect to the device and enter the 2.4G Wi-Fi SSID and password.
5. After connection succeeds, the device saves the configuration and connects automatically on later boots.

To reprovision Wi-Fi after the firmware is running, use one of these methods:

- Click the Boot button during startup to enter provisioning.
- Request reprovisioning through the MCP tool `self.system.reconfigure_wifi`.
- Clear NVS or erase data during flashing, then reboot.

## 5. Buttons and Basic Interaction

| Operation | Function |
|-----------|----------|
| Hold power button for about 3 seconds | Power on/off, depending on the power management circuit state |
| Click Boot | Enter provisioning during startup; toggle conversation state during runtime |
| Double-click Boot | Toggle device-side AEC while idle, when `CONFIG_USE_DEVICE_AEC` is enabled |
| Hold Boot for about 3 seconds | Enter NES game mode |
| Press GPIO10/PTT | Start voice listening |
| Release GPIO10/PTT | End voice listening |
| Tap or swipe touch screen | Depends on the current firmware UI and application logic |

## 6. Voice Assistant

### 6.1 Conversation

1. Make sure the device is connected to Wi-Fi.
2. Click Boot to switch to conversation/listening state, or hold GPIO10/PTT to start speaking.
3. Speak your question or command.
4. Release PTT or wait for the device to stop listening.
5. The device plays the response through the speaker and updates the screen state.

### 6.2 AEC Switching

Device-side AEC suppresses speaker echo. When enabled in firmware, double-click Boot while idle to toggle AEC. If the device frequently captures its own speaker output during recognition, try enabling AEC. In simpler acoustic environments, you may disable it to reduce processing load.

## 7. SD Card Usage

### 7.1 Format and Directories

Format the MicroSD card as FAT32 and create directories as needed:

```text
/sdcard
├── music
│   ├── song1.mp3
│   └── song2.mp3
├── test.mp3
├── nes
│   ├── game1.nes
│   └── game2.nes
└── videos
    ├── demo.mjpg
    ├── demo.mp3
    └── demo.fps
```

### 7.2 Check SD Card Mounting

If the startup log contains `SD card mounted at /sdcard`, the card mounted successfully. You can also call `self.media.list_mp3_files` to check whether MP3 files can be read.

## 8. Local MP3 Playback

### 8.1 Supported Tools

| Function | MCP tool |
|----------|----------|
| Play a specific MP3 | `self.media.play_mp3` |
| Stop playback | `self.media.stop_mp3` |
| List MP3 files | `self.media.list_mp3_files` |
| Play a test file | `self.media.play_test_mp3` |
| Get playback state | `self.media.get_mp3_state` |
| Next track | `self.media.play_next` |
| Previous track | `self.media.play_previous` |

### 8.2 Examples

Play music from the SD card:

```json
{
  "tool": "self.media.play_mp3",
  "arguments": {
    "filepath": "/sdcard/music/song1.mp3"
  }
}
```

List MP3 files under `/sdcard`:

```json
{
  "tool": "self.media.list_mp3_files",
  "arguments": {
    "directory": "/sdcard"
  }
}
```

## 9. Internet Radio

After the device is online, internet radio tools can play network audio streams.

| Function | MCP tool |
|----------|----------|
| Play station | `self.radio.play_url` |
| Stop radio | `self.radio.stop` |
| Get status | `self.radio.get_status` |

Example:

```json
{
  "tool": "self.radio.play_url",
  "arguments": {
    "station_name": "Hit FM"
  }
}
```

## 10. NES Game Mode

### 10.1 Prepare ROMs

Create a `nes` directory in the SD card root and place `.nes` files inside:

```text
/sdcard/nes
├── Super Mario Bros.nes
├── Contra.nes
└── Tetris.nes
```

### 10.2 Enter Game Mode

1. Make sure the device is idle.
2. Hold the Boot button for about 3 seconds.
3. The screen enters the NES game menu.
4. The device scans for Bluetooth HID gamepads.
5. Put the gamepad into pairing mode and wait for connection.
6. Use the gamepad to select a ROM and start the game.

### 10.3 Gamepad Controls

| Gamepad button | Function |
|----------------|----------|
| D-pad | Menu selection or in-game direction |
| A / Start | Start game in menu |
| A | NES A |
| B | NES B |
| Start | NES Start |
| Select | NES Select |
| Start + Select | Return to menu in game; exit game mode in menu |
| Short press Start + Select | Pause/resume, depending on current game state |
| Hold L1 + R1 for about 2 seconds | Reset game |

### 10.4 ROM Compatibility

Mapper support listed in the current firmware documentation includes 0, 1, 2, 3, and 4. If a game shows a black screen, corrupted graphics, or stuttering, try another ROM or a more common mapper version.

## 11. RGB LED and Smart Home MQTT

### 11.1 Direct RGB Control

Set the RGB LED:

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

Turn off the RGB LED:

```json
{
  "tool": "self.light.turn_off",
  "arguments": {}
}
```

### 11.2 Configure MQTT

Configure the broker:

```json
{
  "tool": "self.mqtt.configure",
  "arguments": {
    "broker_address": "broker-cn.emqx.io",
    "port": 1883,
    "client_id": "bigsmart_001",
    "use_tls": false
  }
}
```

Connect MQTT:

```json
{
  "tool": "self.mqtt.connect",
  "arguments": {}
}
```

Subscribe to a light-control topic:

```json
{
  "tool": "self.mqtt.subscribe_light",
  "arguments": {
    "topic": "home/living_room/light"
  }
}
```

Supported light-control message example:

```json
{"state":"ON","brightness":80,"color":{"r":255,"g":100,"b":50}}
```

### 11.3 Publish Control Messages

```json
{
  "tool": "self.mqtt.publish",
  "arguments": {
    "topic": "home/living_room/humidifier",
    "payload": "{\"state\":\"ON\"}",
    "qos": 0
  }
}
```

## 12. IMU Attitude and Shake Detection

BigSmart includes a QMI8658 six-axis sensor. After firmware startup, sensor data is read periodically and shake detection is started. You can read attitude angles, acceleration, and gyroscope data through MCP tools:

```json
{
  "tool": "self.imu.get_attitude_angles",
  "arguments": {}
}
```

Typical uses:

- Shake to wake or switch UI.
- Motion-controlled mini games.
- Device attitude display.
- Interactive installation triggers.

## 13. Camera Usage

BigSmart uses a GC0308 camera with 640 x 480 @ 16 FPS hardware support. The reference firmware uses lazy initialization: the camera is not initialized during startup and is only initialized on the first camera request, reducing startup memory pressure.

Suggestions:

- Make sure GC0308-related firmware configuration is enabled.
- Call the camera only when image capability is needed to avoid competing with audio, Wi-Fi, and large UI tasks for memory.
- If the image orientation is wrong, check mirror and flip settings in firmware.

## 14. Troubleshooting

| Problem | Possible cause | Solution |
|---------|----------------|----------|
| Computer cannot detect serial port | Charge-only USB cable, missing driver, device not powered | Replace cable, install driver, check power |
| Flashing fails | Not in download mode or serial port is occupied | Enter download mode with Boot + reset, close serial terminal, retry |
| Cannot connect Wi-Fi | 5G network, wrong password, weak signal | Use 2.4G Wi-Fi, reprovision, move closer to router |
| No sound | Volume too low, amplifier not enabled, audio init failed | Check serial logs and ES8311/ES7210 initialization |
| Poor voice recognition | Noisy environment, too far from mic, unsuitable AEC state | Speak closer to the device, double-click Boot to toggle AEC |
| SD card cannot mount | Not FAT32, poor contact, damaged card | Reformat, reinsert, replace card |
| MP3 not found | Wrong path or unsupported format | Use absolute path and confirm `.mp3` extension |
| NES ROM not found | File not placed in `/sdcard/nes` | Create the directory and copy `.nes` files |
| Gamepad cannot connect | Gamepad not in pairing mode or not HID compatible | Re-enter pairing mode or use a standard Bluetooth HID gamepad |
| MQTT connection fails | Wrong broker address, wrong port, network unreachable | Query `self.mqtt.get_status` and reconfigure broker |

## 15. Hardware Maintenance

- Power off before plugging or unplugging the display, camera, microphone board, or other flex cables.
- Pay attention to battery polarity and charging safety when using battery power.
- Enclosure files are in `enclosure/`. When modifying the structure, consider screen, button, microphone openings, and speaker acoustic cavity.
- Before adding new peripherals, check [Hardware Configuration](hardware.md) to avoid GPIO conflicts.

## 16. References

- Project hardware documentation: [hardware.md](hardware.md)
- Xiaozhi BigSmart firmware reference: `E:\RYMCU\xiaozhi`
- BluFi provisioning documentation: `E:\RYMCU\xiaozhi\docs\blufi.md`
- NES game integration documentation: `E:\RYMCU\xiaozhi\main\boards\rymcu-bigsmart\nes_integration.md`
- MP3 tool documentation: `E:\RYMCU\xiaozhi\main\boards\rymcu-bigsmart\MP3_MCP_TOOLS.md`
- Smart home MQTT documentation: `E:\RYMCU\xiaozhi\main\boards\rymcu-bigsmart\smart_home_mqtt_usage.md`
- EchoEar product reference: https://oshwhub.com/esp-college/echoear
- ESP32-S3 game console workflow reference: https://wiki.lckfb.com/zh-hans/szpi-esp32s3/beginner/game-console.html
