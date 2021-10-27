---
id: features
title: Choosing Firmnware Platform
sidebar_label: Choosing Firmnware Platfor
slug: /features
---

List of implemented features


| **Feature**                                                                                                            | [PiKey](http://pikey.jpconstantineau.com/)  | [Makerdiary Python Keyboard](https://github.com/makerdiary/python-keyboard) |  [KMK](https://github.com/KMKfw/kmk_firmware)  |
| ---------------------------------------------------------------------------------------------------------------------- |  :-------: |  :-------: |  :-------: | 
| License                                                                                                                |    MIT     |  MIT    |  GPLV3 |
| **Connectivity and Power Saving Options**                                                                              |            | | |
| Low Latency BLE Support                                                                                                |     🚧    | ✅  |  ✅ |
| Multi-Device BLE Support (Several Computers)                                                                           |     ❓     |  | |
| USB HID                                                                                                                |     ✅     |  ✅   | ✅  |
| Battery Reporting (BLE Battery Service)                                                                                |     🚧     |   | |
| Low Power Sleep States                                                                                                 |     ❓     |  | |
| Low Active Power Usage                                                                                                 |     ❓       |  | |
| **Firmware Options**                                                                                                   |            |   | |
| Keymaps and Layers                                                                                                     |     ✅     |   | ✅ |
| Basic Keycodes                                                                                                         |     ✅     |  ✅  |  ✅  |
| Basic consumer (Media) Keycodes                                                                                        |     🚧     | ✅  | ✅ |
| Mouse Keys                                                                                                             |     🚧     |   | |  
| Hold-Tap (which includes Mod-Tap and Layer-Tap)                                                                        |     🚧     |   | |
| One Shot Keys                                                                                                          |     🚧     |   | |
| Combo Keys                                                                                                             |     🚧     |   | |
| Macros                                                                                                                 |     ✅     |   | |
| DuckyScipt Macros                                                                                                      |     🚧     |   | |
| **Keyboard and Controller Board Hardware Options**                                                                     |            |     | |
| Ghosted Keys Support                                                                                                   |     🚧     |   | |
| Split Keyboard Support                                                                                                 |     🚧     |  ❌ | ✅  |
| Key Backlight LED PWM Control                                                                                          |     🚧    |   | |
| RGB Underglow                                                                                                          |     🚧     |   | |
| Encoders                                                                                                               |     🚧     |   | |
| OLED Display Support                                                                                                   |     🚧     |  | |
| Audio/Speaker Support                                                                                                  |     🚧     |   | |
| Low Power Mode (VCC Shutoff)                                                                                           |     🚧     |   |   ✅ |
| **Microcontroller Support**                                                                                            |            |     | |
| Support for Nordic nRF52 Microcontrollers  [^1]                                                                        |     ✅     |  ✅  |  ✅  |
| Support for Wide Range of ARM Microcontrollers  [^1]                                                                   |     ✅     |   | |
| Support for AVR/8 Bit Microcontrollers                                                                                 |     ❌     |  ❌   | ❌ |
| **Tooling and Build Configuration**                                                                                    |            |      | |
| Serial Debug CLI [^2]                                                                                                  |      ✅   |     | | 
| Web Bluetooth Configuration                                                                                            |      💡    |    | |
| Hardware Troubleshooting tools                                                                                         |      ✅   |     | |
| Realtime Keymap Updating                                                                                               |      ✅     |  ✅   | ✅ |


This __Features Compared__ page is licenced under [CC-BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) and was adapted from [ZMK Firmware Documentation](https://zmkfirmware.dev/docs/) originally created by the ZMK Project Contributors.

**Notes**

[^1]: Requires CircuitPython Support
[^2]: REPL



