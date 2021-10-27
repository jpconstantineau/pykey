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


class M60(KB_Hardware):
    """
    Class representing a single Keyboard.
    """

    def __init__(self, nkro: bool = False):
        super().__init__(nkro)

        # Hardware definition: Switch Matrix Setup.
        self._keys = keypad.KeyMatrix(
            row_pins=(
                board.R1,
                board.R2,
                board.R3,
                board.R4,
                board.R5,
                board.R6,
                board.R7,
                board.R8,
            ),
            column_pins=(
                board.C1,
                board.C2,
                board.C3,
                board.C4,
                board.C5,
                board.C6,
                board.C7,
                board.C8,
            ),
            columns_to_anodes=True,
        )
