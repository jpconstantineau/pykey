---
id: findingmatrix
title: Finding Key Matrix
sidebar_label: Finding Key Matrix
---

The following program will list the GPIO names connected to anodes and cathodes of a keyboard matrix. Open up the serial connection to the REPL and press keys in sequence.  Make sure you go through each row and column methodically so that the order printed out makes sense.

If no diodes are in the key matrix, you may see pins listed in both anodes and cathodes.  With this list you will have a starting point on how to configure the keypad scanning routines.

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
        pin.pull = Pull.DOWN
        if pin not in pins:
            pins.append([scl_pin, pin])


anodes=[]
cathodes = []

while True:
    for row in pins:
        row[1].direction = Direction.OUTPUT
        row[1].value = True
        for column in pins:
            if row is column:
                continue
            column[1].direction = Direction.INPUT
            column[1].pull = Pull.DOWN    
               
            if column[1].value:
                if row[0] not in anodes:
                    anodes.append(row[0])
                if column[0] not in cathodes:
                    cathodes.append(column[0])
    print('anodes', end=' ')
    print(anodes)
    print('cathodes', end=' ')
    print(cathodes)
    time.sleep(0.2)
```