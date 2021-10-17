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


class VColChoc44(KB_Hardware):
    """
    Class representing a single Keyboard.
    """

    def __init__(self, nkro: bool = False):
        super().__init__(nkro)

        # Hardware definition: Switch Matrix Setup.
        self._keys = keypad.KeyMatrix(
            row_pins=(board.ROW1, board.ROW2, board.ROW3, board.ROW4),
            column_pins=(
                board.COL1,
                board.COL2,
                board.COL3,
                board.COL4,
                board.COL5,
                board.COL6,
                board.COL7,
                board.COL8,
                board.COL9,
                board.COL10,
                board.COL11,
            ),
            columns_to_anodes=True,
        )

        self._pixels = neopixel.NeoPixel(
            board.NEOPIXEL, 44, brightness=1, auto_write=False
        )

        self._speaker = KB_Speaker(board.SPEAKER)

        # The following should like a columns x row matrix with numbers indicating pixel ID per key
        # The following should like a columns x row matrix with numbers indicating pixel ID per key
        self._key_to_position = (
            0,
            1,
            2,
            3,
            4,
            15,
            39,
            40,
            41,
            42,
            43,
            5,
            6,
            7,
            8,
            9,
            21,
            34,
            35,
            36,
            37,
            38,
            10,
            11,
            12,
            13,
            14,
            28,
            29,
            30,
            31,
            32,
            33,
            16,
            17,
            18,
            19,
            20,
            22,
            23,
            24,
            25,
            26,
            27,
        )
        # the following is to revert back from pixel to key. useful for testing.
        self._position_to_key = (
            0,
            1,
            2,
            3,
            4,
            11,
            12,
            13,
            14,
            15,
            22,
            23,
            24,
            25,
            26,
            5,
            33,
            34,
            35,
            36,
            37,
            16,
            38,
            39,
            40,
            41,
            42,
            43,
            27,
            28,
            29,
            30,
            31,
            32,
            17,
            18,
            19,
            20,
            21,
            6,
            7,
            8,
            9,
            10,
        )
