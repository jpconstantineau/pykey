# SPDX-FileCopyrightText: Copyright (c) 2021 Pierre Constantineau
#
# SPDX-License-Identifier: MIT
"""
`jpconstantineau_pykey60`
================================================================================
A helper library for JPConstantineau's EncoderPads (Basic, Pro/Wireless, RP2040 (RGB))
* Author(s): Pierre Constantineau

Implementation Notes
--------------------
**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's CircuitPython NeoPixel library:
  https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel

* Adafruit's CircuitPython HID library:
  https://github.com/adafruit/Adafruit_CircuitPython_HID

"""

import time
import board
import os
import keypad
import neopixel


from pykey.hardware import KB_Hardware
from pykey.ledmatrix import KB_LEDMatrix
from pykey.speaker import KB_Speaker

class PyKey60(KB_Hardware):
    """
    Class representing a single Keyboard.
    """

    def __init__(self, nkro: bool = False):
        super().__init__(nkro)

        # Hardware definition: Switch Matrix Setup.
        self._keys = keypad.KeyMatrix(
            row_pins=(board.ROW1, board.ROW2, board.ROW3, board.ROW4, board.ROW5),
            column_pins=(board.COL1, board.COL2, board.COL3, board.COL4, board.COL5, board.COL6, board.COL7,
                        board.COL8, board.COL9, board.COL10, board.COL11, board.COL12, board.COL13, board.COL14),
            columns_to_anodes=True,
        )

        self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 61, brightness=1, auto_write=False)

        self._speaker = KB_Speaker(board.SPEAKER)
