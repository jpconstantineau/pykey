---
id: basic
title: Basic GPIOs
sidebar_label: Basic GPIOs
---

For basic information on how to use GPIOs in CircuitPython, refer to this great tutorial from [Adafruit](https://learn.adafruit.com/circuitpython-digital-inputs-and-outputs).

## What GPIOs are available?

We assume you know how to get to REPL. To get the list of GPIOs on your board enter these commands in REPL:

``` python
import board
dir(board)
```

See some simple example in a [video](https://youtu.be/M7GHp6md2Qc?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)

You will get a list of the identifiers on how to call each GPIO for your controller.  These identifiers are what you need when defining the connections to the keyboard.

## Test Outputs: LEDs

The easiest way to test your board and LEDs is to use a simple **blink** program.  You can modify the `LED Setup` section to select the GPIO where your LED is connected to the board.  Change `board.RED_LED` to the GPIO you want to test.  Try the example below by changing the pin definition

``` python
import board
from digitalio import DigitalInOut, Direction
import time

# LED setup.
led = DigitalInOut(board.RED_LED)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```
Once running, you should see the LED blink at a rate of once per second.


## Test Inputs: Switches/Buttons

To help test and identify the GPIOs connected to Switches (ones directly wired between the GPIO and GND), you can use the following program and modify the `LED Setup` and `Switch Setup` sections.  Run the program above to validate that there is a LED on the GPIO you select.

Try the example below by changing the pin definition

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

    time.sleep(0.01) 
```

By pressing the switch, you will turn on the LED.
See a similar example in a [video](https://youtu.be/37R2OVGrV2w?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)

PWM Video example: [here](https://youtu.be/Kelr2DD39g8?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)
