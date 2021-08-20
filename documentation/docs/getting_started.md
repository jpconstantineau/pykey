---
id: getting_started
title: Getting Started
sidebar_label: Getting Started
slug: /
---


## Get some supported hardware. 

Lots of hardware can run PyKey! Keyboards that support one of the boards listed in the [CircuitPython Downloads](https://circuitpython.org/downloads) is a good start. 

## Install CircuitPython on it

Go [here](https://circuitpython.org/downloads) and download the latest CircuitPython for you hardware.  PyKey uses features included in CircuitPython 7.0.0.  You can download the Absolute Newest (automated builds) or the latest 7.0.0 alpha (release). Don't download a 6.x release as some of the necessary modules have only been included since 7.0.0.

## Download and Install the CircuitPython Libraries

You will need to download the libraries from [here](https://circuitpython.org/libraries).
Since there are hundreds of different libraries included in the package, they generally won't fit if you copy them all to yur board. As such, you only need to copy the ones that are needed.

## Read the basics of CircuitPython

Adafruit has created great documentation on how to start with CircuitPython:

* [Essentials](https://learn.adafruit.com/circuitpython-essentials)
* [Pins and Modules](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules) 

## Hardware Setup

### Input Devices
* Buttons: Single keys connected between GPIO and GND
* Key Matrix: Matrix of keys with diodes. Columns and rows are connected to GPIOs: [5x6](https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart/circuitpython) [keypad](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython)
* Rotary Encoders: A and B connected to GPIOs.
* Potentiometers: An Analog value...
* Nunchuck and other digital input devices
* Battery Level: Analog read of battery voltage.
* USB Connection: is it connected to computer through USB?

### Output devices
* LED: Single LED connected to GPIO
* PWM LED: A number of LEDs connected to a Mosfet for PWM intensity control.
* LED Matrix: matrix of LEDs, Columns and Rows are connected to GPIOs
* RGB LEDs: addressable LEDs.
* Speaker: Single speaker connected to as GPIO
* Displays: Too many types to count...
* Serial port: useful for debugging...

### HID Profiles
* Keyboard - standard keycodes
* Keyboard - consumer
* Mouse
* Gamepad

### HID Connections
* USB HID
* [BLE HID](https://learn.adafruit.com/ble-hid-keyboard-buttons-with-circuitpython)

## Keymap Setup

## Main Loop

