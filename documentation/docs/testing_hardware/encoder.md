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

If you want to see an example of how to read a retary encoder, see this [video](https://youtu.be/4BNkuLonIVM?list=PLjF7R1fz_OOWFqZfqW9jlvQSIUmwn9lWr)