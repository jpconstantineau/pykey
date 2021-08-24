---
id: findingbuttons
title: Finding Buttons
sidebar_label: Finding Buttons
---

The following program will list the button GPIO names when you press the buttons.
This assumes that the buttons have one side grounded and the other connected to the controller.

With this list you will have a starting point on how to configure the key scanning routines.

``` python
import board
import time
from microcontroller import Pin
from digitalio import DigitalInOut, Direction, Pull

def get_unique_pins():
    exclude = ['NEOPIXEL', 'APA102_MOSI', 'APA102_SCK']
    pins = [pin for pin in [
        getattr(board, p) for p in dir(board) if p not in exclude]
            if isinstance(pin, Pin)]
    unique = []
    for p in pins:
        if p not in unique:
            unique.append(p)
    return unique

pins = []

for scl_pin in get_unique_pins():
        pin = DigitalInOut(scl_pin)
        pin.direction = Direction.INPUT
        pin.pull = Pull.UP
        if pin not in pins:
            pins.append([scl_pin, pin])

while True:
    for item in pins:
        if not item[1].value :
            print(item[0])
    time.sleep(0.2)
```