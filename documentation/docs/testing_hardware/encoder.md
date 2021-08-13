---
id: encoders
title: Rotary Encoders
sidebar_label: Rotary Encoders
---

For basic information on rotary encoders, refer to this great tutorial from [Adafruit](https://learn.adafruit.com/rotary-encoder)


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