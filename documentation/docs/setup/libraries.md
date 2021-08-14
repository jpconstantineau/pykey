---
id: libraries
title: Libraries Needed
sidebar_label: Libraries Needed
---

The PyKey firmware needs a number of libraries to be available on the board for it to run.

| **Library/Module**                                                   |  Import (with link to docs)            | Files/Folder needed |
| :------------------------------------------------------------------- |  :-------           |  :-------    | 
| **Default Modules**                                                  |                     |              |
| GPIO Definition                                                      |  [import board](https://circuitpython.readthedocs.io/en/latest/shared-bindings/board/index.html)       |              |
| GPIO Access                                                          |  [import digitalio](https://circuitpython.readthedocs.io/en/latest/shared-bindings/digitalio/index.html)   |              |
| Key Matrix and Switches                                              |  [import keypad](https://circuitpython.readthedocs.io/en/latest/shared-bindings/keypad/index.html)      |              |
| Basic Sound/Buzzer                                                   |  [import pwmio](https://circuitpython.readthedocs.io/en/latest/shared-bindings/pwmio/index.html)       |              |
| PWM/Dimming LEDs                                                     |  [import pwmio](https://circuitpython.readthedocs.io/en/latest/shared-bindings/pwmio/index.html)       |              |           
| RGB LEDs - color wheel                                               |  [import rainbowio](https://circuitpython.readthedocs.io/en/latest/shared-bindings/rainbowio/index.html)   |              |
| Rotary Encoders                                                      |  [import rotaryio](https://circuitpython.readthedocs.io/en/latest/shared-bindings/rotaryio/index.html)    |              |
| Sleep/delay                                                          |  [import time](https://circuitpython.readthedocs.io/en/latest/shared-bindings/time/index.html)        |              |
| USB Human Interface Device Definition                                |  [import usb_hid](https://circuitpython.readthedocs.io/en/latest/shared-bindings/usb_hid/index.html)     |              |
|  [**Adafruit CircuitPython Library Bundle**](https://circuitpython.org/libraries)                                   |                     |              |
| Keyboard USB HID                                                     |  from [adafruit_hid.keyboard](https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html) import Keyboard    | adafruit_hid |
| RGB LEDs - Access                                                    |  [import neopixel](https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html)    | neopixel.mpy |


PyKey uses libraries from the [Adafruit CircuitPython Library Bundle 7.x](https://circuitpython.org/libraries).



Installing Libraries is as simple as copying the files into the lib folder.