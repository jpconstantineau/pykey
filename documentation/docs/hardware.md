---
id: hardware
title: Choosing Hardware Platform
sidebar_label: Choosing Hardware Platform
---

Here is a comparative table to help choose the processor and base hardware to build your keyboard.
Note that not all features and not all hardware form factors are shown.

| **Feature**            |  SAMD21     | SAMD51      | RP2040      |  nRF52840  | STM32F4 | ESP32-S2 |
| ---------------------- | :---------  |  :-------   | :-------    |  :-------  | :-------  | :-------  |
| **Processor**          |  Cortex M0+ |  Cortex M4F | Cortex M0+  | Cortex M4F | Cortex M4F | Xtensa LX7 |
| Speed                  |  48 MhZ     |  120 Mhz    | 133MHz      | 64 MHz     | 168 MHz     | 240MHz  |
| Ram                    |  32KB       |  192KB      | 264KB     | 256KB      | 192KB      | 320KB + External    |
| Base Flash             |  256KB      |  512KB      | External 2MB | 1MB       | 1MB       | External |
| Hardware Features      |             |             | 2 cores, PIO | BLE |   |  WiFi  |
| **CircuitPython Core Modules** |     |             |              |           |
| _bleio |  ❌   |     ✅        |        ✅      |     ✅      |  ✅      | ✅      |
| alarm:  |  ❌   |     ❌        |        ✅      |     ✅      |  ✅      | ✅      |
| analogio:  |  ✅   |     ✅        |        ✅      |     ✅      |  ✅      | ✅      |
| board:  |  ✅   |     ✅        |        ✅      |     ✅      |  ✅      | ✅      |
| digitalio:  |  ✅   |     ✅        |        ✅      |     ✅      |  ✅      | ✅      |
| displayio: | ❌   |      ✅       |   ✅           |     ✅      |  ✅      | ✅      |
| keypad:   |  ❌   |      ✅       |   ✅           |     ✅      |  ✅      |  ✅      |
| neopixel_write:    |  ✅   |      ✅       |  ✅            |     ✅      |  ✅      | ✅      |
| pwmio:    |  ✅   |      ✅       |  ✅            |     ✅      |  ✅      | ✅      |
| rotaryio: |  ✅   |      ✅       | ✅             |     ✅        |  ❌      | ✅      |
| time: |  ✅   |      ✅       | ✅             |     ✅        | ✅        | ✅      |
| touchio:  |  ✅   |      ✅       |   ✅           |     ✅      | ✅        | ✅      |
| usb_hid:  |  ✅   |      ✅       |   ✅           |     ✅      | ✅        | ✅      |
| **Hardware Form Factors**  |       |                      |                   |                            | |  |
| Dongle Form  | Trinkey SAMD21        |                      |                   | nRF52840 Dongle            | |  |
| 5 GPIOs      | Trinket M0            |                      |                   |                            | |  |
| 11 GPIOs     | QT Py, Seeeduino XIAO |                      | QT Py RP2040      |                            | |  |
| 18 GPIOs     |                       |                      | Pro Micro RP2040  | BlueMicro840, Nice!Nano    | |  |
| 21 GPIOs     | Feather M0 Express    | Feather M4 Express   | Feather RP2040    | Feather nRF52840 Express   | Feather STM32F405 Express |  |
| 21-23 GPIOs  | ItsyBitsy M0 Express  | ItsyBitsy M4 Express | ItsyBitsy RP2040  | ItsyBitsy nRF52840 Express | |  |
| 26 GPIOs     |                       |                      | Pi Pico           |                            | |  |
| Finished Products |                   | NeoTrellis M4        | MacroPad RP2040, Keybow 2040, PyKey60, EncoderPad RP2040   | M60 Mechanical Keyboard| |  |

Comments:

* STM boards do not have rotaryio implemented yet.
* Due to limited RAM and flash size, CircuitPython builds for SAMD21 boards only include the bare minimum core modules.
* Low clock speeds for nRF52840 allows for lower power usage and longer battery life for BLE applications.

                                        








