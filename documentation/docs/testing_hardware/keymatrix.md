---
id: keymatrix
title: Key Matrix
sidebar_label: Key Matrix
---



``` python
import board
import keypad

keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_03, board.P0_28, board.P1_13),
    column_pins=(board.P0_02, board.P0_29, board.P0_30, board.P0_26),
    columns_to_anodes=True,
)


while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)

```