# SPDX-FileCopyrightText: Copyright (c) 2021 Pierre Constantineau
#
# SPDX-License-Identifier: MIT
"""
`jpconstantineau_encoderpad`
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
import rotaryio

from pykey.hardware import KB_Hardware
from pykey.ledmatrix import KB_LEDMatrix
from pykey.speaker import KB_Speaker

class EncoderPad(KB_Hardware):
    """
    Class representing a single EncoderPad.
    """

    def __init__(self, nkro: bool = False):
        super().__init__(nkro)

        # Below are Basic EncoderPads
        if 'Adafruit QT Py RP2040' in self._board_type:
            print("EncoderPad Basic with QT Py RP2040")
            self._keys = keypad.Keys((board.D7, board.D8, board.D9,
                                      board.D10, board.D0, board.D1,
                                      board.D2, board.D3, board.D6),
                                    value_when_pressed=False, pull=True)
            self._encoder = rotaryio.IncrementalEncoder(board.D4, board.D5)
            # HARDWARE BUG - D6 and D5 are not sequential GPIOs but D4 and D5 are...
            # rotary encoder is located on D5 and D6. A new version of the PCB is needed...
            # see https://github.com/adafruit/circuitpython/issues/5334
        elif 'Adafruit QT Py M0 Haxpress' in self._board_type:
            raise ValueError("QT Py M0 non-KB version not supported")
        elif 'Adafruit QT Py M0' in self._board_type:
            raise ValueError("QT Py M0 non-KB version not supported")
        elif 'Seeeduino XIAO' in self._board_type:
            if 'seeeduino_xiao_kb' in board.board_id:
                print("EncoderPad Basic with XIAO KB version")
                # No pixels, leds or speaker
                self._keys = keypad.Keys((board.D7, board.D8, board.D9,
                                      board.D10, board.D0, board.D1,
                                      board.D2, board.D3, board.D4),
                                    value_when_pressed=False, pull=True)
                self._encoder = rotaryio.IncrementalEncoder(board.D5, board.D6)
            else:
                raise ValueError("XIAO non-KB version not supported")

        # Below are Pro/Wireless EncoderPads
        elif 'SparkFun Pro Micro RP2040' in self._board_type:
            print("EncoderPad Pro with Pro Micro RP2040")
            self._leds = KB_LEDMatrix((board.D1,board.D26,board.D20),(board.D6,board.D4,board.D8),True)
            self._leds.reset_leds()
            self._speaker = KB_Speaker(board.D27)

            self._keys = keypad.KeyMatrix(
                row_pins=(board.D0, board.D22, board.D23),
                column_pins=(board.D7, board.D5,board.D9),
                columns_to_anodes=False,
            )
            self._encoder = rotaryio.IncrementalEncoder(board.D28, board.D29)

        elif 'nice!nano' in self._board_type:
            print("EncoderPad Pro with nice!nano")
            self._leds = KB_LEDMatrix((board.P0_08,board.P1_15,board.P1_11),(board.P1_00,board.P0_22,board.P1_04),True)
            self._leds.reset_leds()
            self._speaker = KB_Speaker(board.P0_02)

            self._keys = keypad.KeyMatrix(
                row_pins=(board.P0_06, board.P1_13, board.P0_10),
                column_pins=(board.P0_11, board.P0_24,board.P1_06),
                columns_to_anodes=False,
            )
            self._encoder = rotaryio.IncrementalEncoder(board.P0_29, board.P0_31)

        elif 'BlueMicro840' in self._board_type:
            print("EncoderPad Pro with BlueMicro840")
            self._leds = KB_LEDMatrix((board.P0_08,board.P0_02,board.P0_03),(board.P0_24,board.P0_20,board.P0_10),True)
            self._leds.reset_leds()
            self._speaker = KB_Speaker(board.P0_29)

            self._keys = keypad.KeyMatrix(
                row_pins=(board.P0_06, board.P1_13, board.P0_28),
                column_pins=(board.P0_09, board.P0_13,board.P1_06),
                columns_to_anodes=False,
            )
            self._encoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_30)

        # Below is a RGB EncoderPad
        elif 'EncoderPad RP2040' in self._board_type:
            print("EncoderPad RP2040")
            import neopixel
            self._pixels = neopixel.NeoPixel(board.NEOPIXEL, 9)
            self._speaker = KB_Speaker(board.SPEAKER)

            self._keys = keypad.Keys((board.KEY1, board.KEY2, board.KEY3,
                                      board.KEY4, board.KEY5, board.KEY6,
                                      board.KEY7, board.KEY8, board.KEY8),
                                    value_when_pressed=False, pull=True)
            self._encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)

