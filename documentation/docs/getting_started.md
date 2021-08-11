---
id: getting_started
title: Getting Started
sidebar_label: Getting Started
slug: /
---

Not sure yet...  Work in Progress.



# Getting Started

Get some supported hardware.
Get a supported version of CircuitPython.  Download it [here](https://circuitpython.org/downloads).  PyKey uses features included in CircuitPython 7.0.0.

Latest builds are available [here](https://adafruit-circuit-python.s3.amazonaws.com/index.html?prefix=bin/)

Needs the following modules:
* analogio
* board
* digitalio
* keypad
* pwmio
* rotaryio
* time
* usb_hid

Need the following libraries:


From: https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules

import board
dir(board)



# Read basics
https://learn.adafruit.com/circuitpython-essentials


# Hardware Setup

## Input Devices
* Buttons: Single keys connected between GPIO and GND
* Key Matrix: Matrix of keys with diodes. Columns and rows are connected to GPIOs: https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart/circuitpython

https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython

* Rotary Encoders: A and B connected to GPIOs.
* Potentiometers: An Analog value...
* Nunchuck and other digital input devices
* Battery Level: Analog read of battery voltage.
* USB Connection: is it connected to computer through USB?

## Output devices
* LED: Single LED connected to GPIO
* PWM LED: A number of LEDs connected to a Mosfet for PWM intensity control.
* LED Matrix: matrix of LEDs, Columns and Rows are connected to GPIOs
* RGB LEDs: addressable LEDs.
* Speaker: Single speaker connected to as GPIO
* Displays: Too many types to count...
* Serial port: useful for debugging...

## HID Profiles
* Keyboard - standard keycodes
* Keyboard - consumer
* Mouse
* Gamepad

## HID Connections
* USB HID
* BLE HID - https://learn.adafruit.com/ble-hid-keyboard-buttons-with-circuitpython

# Keymap Setup

# Main Loop

