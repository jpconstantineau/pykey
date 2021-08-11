---
id: basic
title: Basic GPIOs
sidebar_label: Basic GPIOs
---


For basic information on how to use GPIOs in CircuitPython, refer to this [page](https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs)



``` python
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.RED_LED)
led.direction = Direction.OUTPUT

# Switch setup.
switch = DigitalInOut(board.P0_30)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:

    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
```

miniMACRO5:

MATRIX_COL_PINS { 30, 43, 28, 24, 10}

ENCODER_PAD_A  {26, 8, 15, 17, 9 }

ENCODER_PAD_B  {6, 29, 2, 20, 13 }