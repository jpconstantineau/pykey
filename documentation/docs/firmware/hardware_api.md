---
id: hardware_api
title: PyKey Hardware API
sidebar_label: Hardware API
---

## Implementation Notes

The PyKey hardware API is inspired from Adafruit's `adafruit_macropad` library for the [Adafruit MacroPad RP2040](https://www.adafruit.com/product/5128)


**Class** jpconstantineau_pykey.KB_Hardware

#### Input Hardware

_property_ **encoder**:   The rotary encoder relative rotation position. Always begins at 0 when the code is run, so the value returned is relative to the initial location.

_property_ **keys**:  The keys on the keyboard. Uses events to track key number and state, e.g. pressed or released. You must fetch the events using ``keys.events.get()`` and then the events are available for usage in your code.

#### Output Hardware

_property_ **pixels**: Sequence-like object representing the NeoPixel LEDs on the keyboard.

_property_ **speaker**: Object representing a speaker or buzzer on the keyboard.


#### USB HID devices 


_property_ **keyboard**: A keyboard object (adafruit_hid.keyboard) used to send HID reports. For details, see the ``Keyboard`` documentation in [CircuitPython HID](https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html) 

_property_ **consumer_control**  A consumer_control object (adafruit_hid.consumer_control) used to send HID reports. For details, see the ``consumer_control`` documentation in [CircuitPython HID](https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html)  HID Object based on adafruit_hid.consumer_control

_property_ **mouse**  A mouse object (adafruit_hid.mouse) used to send HID reports. For details, see the ``Mouse`` documentation in [CircuitPython HID](https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html) HID Object based on adafruit_hid.mouse

#### USB HID Report Helpers
_property_ **keyboard_layout** Map ASCII characters to appropriate keypresses on a  keyboard of a specific layout. For details, see the ``keyboard_layout_us`` documentation in [CircuitPython HID](https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html) HID Object based on adafruit_hid.keyboard_layout_us

Forr other layouts use those defined [here](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts)

#### USB HID Report Codes

**Keycode**  List of constants with all the keycodes. HID Object based on adafruit_hid.keyboard

**ConsumerControlCode** List of constants with all the Consumer Control Codes.  HID Object based on adafruit_hid.consumer_control_code
