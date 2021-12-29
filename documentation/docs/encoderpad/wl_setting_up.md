---
id: wl_setting_up
title: Setting up Wireless Encoderpad
sidebar_label: Setting up Wireless Encoderpad
---
The following assumes you have a BlueMicro840 controller.  If yours uses a Xiao or a RP2040, see the other guides.


## With CircuitPython and PyKey firmware

### Install CircuitPython

- Go to [CircuitPython.Org Download page](https://circuitpython.org/board/bluemicro840/) of the BlueMicro840.
- Download the latest stable release (more recent ones are OK)
- Put the Blurmicro840 in bootloader mode by double-pressing reset
- A new drive called "BLUEMICRO" should show up on your computer
- Copy CircuitPython UF2 file you just downloaded to that drive.
- Once copied, the BlueMicro840 should reset itself and a new drive called "CIRCUITPY" should show up
- CircuitPython is now installed.  

### Install Core Libraries

- Go to [CircuitPython.Org Libraries page](https://circuitpython.org/libraries).
- Download the Bundle for Version 7.x
- Uncompress the bundle
- Copy the following libraries into the lib folder of the "CIRCUITPY" drive
  - adafruit_hid
  - adafruit_ble
  - adafruit_ble_adafruit
  - neopixel.mpy

### Install PyKey Library

- Copy the whole pykey folder from the PyKey [repo](https://github.com/jpconstantineau/pykey/tree/main/pykey) into the root of the "CIRCUITPY" drive


## Copy the example firmware

- Go to the example folder of the Pykey [repo](https://github.com/jpconstantineau/pykey/tree/main/examples/CNCEncoderPad)
- Copy the whole layers folder from the PyKey [repo](https://github.com/jpconstantineau/pykey/tree/main/examples/CNCEncoderPad) into the root of the "CIRCUITPY" drive
- Copy code.py to the root of the "CIRCUITPY" drive (overwrite the existing one)


## With KMK


**Notes:  KMK does not support speaker or the back-lit LEDs of the CNCEncoderpad**

- Install CircuitPython as per instructions for PyKey firmware
- Install core libraries as per instructions for PyKey firmware
- Copy the whole KMK folder from the KMK [repo](https://github.com/jpconstantineau/pykey/tree/main/pykey) into the root of the "CIRCUITPY" drive



## With Arduino

## With BlueMicro_BLE