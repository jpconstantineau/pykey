---
id: encoders
title: Rotary Encoders
sidebar_label: Rotary Encoders
---

``` python
import board
import rotaryio

encoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)
last_position = None
while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position

    ``` 