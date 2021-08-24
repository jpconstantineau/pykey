---
id: encoders
title: Rotary Encoders
sidebar_label: Rotary Encoders
---

## Rotary Encoder

For basic information on rotary encoders, refer to this great tutorial from [Adafruit](https://learn.adafruit.com/rotary-encoder)

## Basic Test

``` python
import board
import rotaryio

# Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position

``` 

If you want to see an example of how to read a rotary encoder, see this [video](https://youtu.be/4BNkuLonIVM?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)

## miniMacro5 - 5 Encoders Test

CircuitPython seems to only support up to 4 rotary encoders.

``` python
import board
import rotaryio

# Encoder Setup
encoder1 = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)
encoder2 = rotaryio.IncrementalEncoder(board.P0_08, board.P0_29)
encoder3 = rotaryio.IncrementalEncoder(board.P0_15, board.P0_02)
encoder4 = rotaryio.IncrementalEncoder(board.P0_17, board.P0_20)
encoder5 = rotaryio.IncrementalEncoder(board.P0_09, board.P0_13)

last_position1 = None
last_position2 = None
last_position3 = None
last_position4 = None
last_position5 = None
while True:
    position1 = encoder1.position
    position2 = encoder2.position
    position3 = encoder3.position
    position4 = encoder4.position
    position5 = encoder5.position
    if last_position1 is None or position1 != last_position1:
        print(position1, position2, position3, position4, position5)
    if last_position2 is None or position2 != last_position2:
        print(position1, position2, position3, position4, position5)
    if last_position3 is None or position3 != last_position3:
        print(position1, position2, position3, position4, position5)
    if last_position4 is None or position4 != last_position4:
        print(position1, position2, position3, position4, position5)
    if last_position5 is None or position5 != last_position5:
        print(position1, position2, position3, position4, position5)
    last_position1 = position1
    last_position2 = position2
    last_position3 = position3
    last_position4 = position4
    last_position5 = position5
``` 