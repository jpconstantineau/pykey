---
id: getting_started
title: Getting Started
sidebar_label: Getting Started
slug: /
---


Get some supported hardware.
Get a supported version of CircuitPython.  Download it [here](https://circuitpython.org/downloads).  PyKey uses features included in CircuitPython 7.0.0.
You can download the Absolute Newest (automated builds) or the latest 7.0.0 alpha (release). Don't download a 6.x release as some of the necessary modules have only been included since 7.0.0.


You will also need to download the libraries from [here](https://circuitpython.org/libraries).



# Read the basics

Adafruit has created great documentation on how to start with CircuitPython:

* [Essentials](https://learn.adafruit.com/circuitpython-essentials)
* [Pins and Modules](https://learn.adafruit.com/circuitpython-essentials/circuitpython-pins-and-modules) 

# Hardware Setup

## Input Devices
* Buttons: Single keys connected between GPIO and GND
* Key Matrix: Matrix of keys with diodes. Columns and rows are connected to GPIOs: [5x6](https://learn.adafruit.com/adafruit-neokey-5x6-ortho-snap-apart/circuitpython) [keypad](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython)
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
* [BLE HID](https://learn.adafruit.com/ble-hid-keyboard-buttons-with-circuitpython)

# Keymap Setup

# Main Loop

