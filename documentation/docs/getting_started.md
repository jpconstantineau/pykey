---
id: getting_started
title: Getting Started
sidebar_label: Getting Started
slug: /
---

# What is PyKey?

**PyKey** or "**Py**thon**Key**board" is a CircuitPython firmware based on the various examples contained in the [Adafruit learning guides](https://learn.adafruit.com/guides/popular) available in their [GitHub repository](https://github.com/adafruit/Adafruit_Learning_System_Guides).


## Why CircuitPython and not C/C++?
Many Keyboard firmwares are available in C/C++.  Take for example TMK, QMK, BlueMicro_BLE, ZMK and many others.  They all implement a firmware that combine the low-level hardware scanning as well as the high-level keyboard functionality that users want.

With PyKey, the aim is on keeping it simple and away from the hardware-specific details and focussed on the high level keyboard logic.  This therefore makes it more DIY friendly and portable from one platform to another with minimal code chhanges.

With CircuitPython 7.0.0, the most frequently called code in a keyboard firmware (the key scanning and debouncing routines) has been embedded within the core of CircuitPython (in the keypad module) and runs as compiled C++ code.  This reduces significantly the amount of Python code that continuously runs waiting for keys to be pressed; thus improving performance.  The rest of the keyboard logic, which only runs once keypresses are detected, has more time to run between key scans.

CircuitPython also makes it very simple to customize the keymaps and the keyboard logic without any toolchain and without the need to recompile and flash your keyboard.  If you have a text editor and can edit a file saved in a mass storage device, you can make live changes to how your keyboard works.


# Getting Started
## Get some supported hardware. 

 Lots of hardware supports CircuitPython. Currently, 226 boards support it.  Not all are destined to be keyboards. 
 Keyboards that support one of the breakout boards listed in the [CircuitPython Downloads](https://circuitpython.org/downloads) is a good start.  There are even macropads in the list.

 Here are a few examples in pictures:


| [![Pico](https://circuitpython.org/assets/images/boards/small/raspberry_pi_pico.jpg)](https://circuitpython.org/board/raspberry_pi_pico/)    | [![Feather840](https://circuitpython.org/assets/images/boards/small/feather_nrf52840_express.jpg) ](https://circuitpython.org/board/feather_nrf52840_express/)| [![ItsyBitsy M4](https://circuitpython.org/assets/images/boards/small/itsybitsy_m4_express.jpg)](https://circuitpython.org/board/itsybitsy_m4_express/) |
| :---: | :---: |  :---: | 
| [![blueMicro840](https://circuitpython.org/assets/images/boards/small/bluemicro840.jpg)](https://circuitpython.org/board/bluemicro840/) | [![NiceNano](https://circuitpython.org/assets/images/boards/small/nice_nano.jpg) ](https://circuitpython.org/board/nice_nano/)                  |  [![Pro micro RP2040](https://circuitpython.org/assets/images/boards/small/sparkfun_pro_micro_rp2040.jpg)](https://circuitpython.org/board/sparkfun_pro_micro_rp2040/) |
| [![macropad](https://circuitpython.org/assets/images/boards/small/adafruit_macropad_rp2040.jpg)](https://circuitpython.org/board/adafruit_macropad_rp2040/) | [![trellis](https://circuitpython.org/assets/images/boards/small/trellis_m4_express.jpg)](https://circuitpython.org/board/trellis_m4_express/) | [![keybow](https://circuitpython.org/assets/images/boards/small/pimoroni_keybow2040.jpg)](https://circuitpython.org/board/pimoroni_keybow2040/)


## Install CircuitPython on it

Go [here](https://circuitpython.org/downloads) and download the latest CircuitPython for your hardware.  PyKey uses features included in CircuitPython 7.0.0.  You can download the Absolute Newest (automated builds) or the latest 7.0.0 alpha (release). Don't download a 6.x release as some of the necessary modules have only been included since 7.0.0.

## Download and Install the CircuitPython Libraries

You will need to download the libraries from [here](https://circuitpython.org/libraries).
Since there are hundreds of different libraries included in the package, they generally won't fit if you copy them all to your board. As such, you only need to copy the ones that are needed.

## Read the basics of CircuitPython

Adafruit has created great documentation on how to start with CircuitPython:

* [What is CicuitPython](https://learn.adafruit.com/welcome-to-circuitpython)
* [Essentials](https://learn.adafruit.com/circuitpython-essentials)
* [Pins and Modules](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules) 

# Possible Hardware

## Input Devices

A number of input devices and methods can be used with CircuitPython:
* Buttons: Single keys connected between GPIO and GND
* Key Matrix: Matrix of keys with diodes. Columns and rows are connected to GPIOs: [5x6](https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart/circuitpython) [keypad](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython)
* Rotary Encoders: A and B connected to GPIOs.
* Potentiometers: An Analog value...
* Nunchuck and other digital input devices
* Battery Level: Analog read of battery voltage.
* USB Connection: is it connected to computer through USB?

## Output devices

Similarly to input devicecs, CircuitPython supports a vast array of feedback methods to the user:

* LED: Single LED connected to GPIO
* PWM LED: A number of LEDs connected to a Mosfet for PWM intensity control.
* LED Matrix: matrix of LEDs, Columns and Rows are connected to GPIOs
* RGB LEDs: addressable LEDs.
* Speaker: Single speaker connected to a GPIO
* Displays: Too many types to count...
* Serial port: useful for debugging...

## HID Profiles
Human Interface Devices define multiple interfaces for interacting with computers:

* Keyboard - standard keycodes
* Keyboard - consumer
* Mouse
* Gamepad

## HID Connections

CircuitPython supports both USB and Bluetooth.

* USB HID
* [BLE HID](https://learn.adafruit.com/ble-hid-keyboard-buttons-with-circuitpython)


