---
id: libraries
title: Libraries Needed
sidebar_label: Libraries Needed
---

| **Library/Module**                                                   |  Import             | Files/Folder needed |
| :------------------------------------------------------------------- |  :-------           |  :-------    | 
| **Default Modules**                                                  |                     |              |
| GPIO Definition                                                      |  import board       |              |
| GPIO Access                                                          |  import digitalio   |              |
| Key Matrix and Switches                                              |  import keypad      |              |
| Basic Sound/Buzzer                                                   |  import pwmio       |              |
| RGB LEDs - color wheel                                               |  import rainbowio   |              |
| Rotary Encoders                                                      |  import rotaryio    |              |
| Sleep/delay                                                          |  import time        |              |
| USB Human Interface Device Definition                                |  import usb_hid     |              |
|  **CircuitPython Library Bundle**                                    |                     |              |
| Keyboard USB HID                                                     |  from adafruit_hid.keyboard import Keyboard    | adafruit_hid |
| RGB LEDs - Access                                                    |  import neopixel    | neopixel.mpy |



