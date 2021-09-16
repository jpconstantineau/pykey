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
import usb_hid
from adafruit_hid.keyboard import Keyboard


class Speaker:

    def __init__(self, speaker_pin):
        import pwmio
        self.speaker_pin = speaker_pin
        self.buzzer = pwmio.PWMOut(speaker_pin, variable_frequency=True)
        self.buzzer.frequency = 440

    def play_startup_tune(self):
        OFF = 0
        ON = 2**15
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 440
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.05)
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.duty_cycle = OFF

    def play_shutdown_tune(self):
        OFF = 0
        ON = 2**15
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.1)
        self.buzzer.frequency = 440
        time.sleep(0.15)
        self.buzzer.duty_cycle = OFF



class LEDMatrix:
# LEDMatrix(row_pins: Sequence[microcontroller.Pin], column_pins: Sequence[microcontroller.Pin], columns_to_anodes: bool = True)


    def __init__(self, row_pins, column_pins, columns_to_anodes: bool = True):
        from digitalio import DigitalInOut, Direction
        self.row_pins = row_pins
        self.column_pins = column_pins
        self.columns_to_anodes = columns_to_anodes
        self.column_io = []
        self.row_io = []
        for cp in self.column_pins:
            self.column_io.append(DigitalInOut(cp))
        for rp in self.row_pins:
            self.row_io.append(DigitalInOut(rp))

    def reset_leds(self):
        for pin in self.row_io:
            pin.direction = Direction.OUTPUT
            pin.value = False
        for pin in self.column_io:
            pin.direction = Direction.OUTPUT
            pin.value = False

    def led_ON(self, led_number):
        self.reset_leds()
        colcount=len(self.column_io)
        colIOLED = self.column_io[0]
        rowIOLED = self.row_io[0]
        for rownum, rowIO in enumerate(self.row_io):
            for colnum, colIO in enumerate(self.column_io):
                if led_number == (rownum * colcount + colnum):
                    colIOLED = colIO
                    rowIOLED = rowIO
                if self.columns_to_anodes:
                    colIO.value = False
                    rowIO.value = True
                else:
                    colIO.value = True
                    rowIO.value = False
        if self.columns_to_anodes:
            colIOLED.value = True
            rowIOLED.value = False
        else:
            colIOLED.value = False
            rowIOLED.value = True

    def led_OFF(self):
        self.reset_leds()



class EncoderPad:
    """
    Class representing a single EncoderPad.
    """

    def __init__(self):

        self._board_type = os.uname().machine
        self._keyboard = None
        self._pixels = None
        self._leds = None
        self._speaker =  None

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
            self._leds = LEDMatrix((board.D1,board.D26,board.D20),(board.D6,board.D4,board.D8),True)
            self._leds.reset_leds()
            self._speaker = Speaker(board.D27)

            self._keys = keypad.KeyMatrix(
                row_pins=(board.D0, board.D22, board.D23),
                column_pins=(board.D7, board.D5,board.D9),
                columns_to_anodes=False,
            )
            self._encoder = rotaryio.IncrementalEncoder(board.D28, board.D29)

        elif 'nice!nano' in self._board_type:
            print("EncoderPad Pro with nice!nano")
            self._leds = LEDMatrix((board.P0_08,board.P1_15,board.P1_11),(board.P1_00,board.P0_22,board.P1_04),True)
            self._leds.reset_leds()
            self._speaker = Speaker(board.P0_02)

            self._keys = keypad.KeyMatrix(
                row_pins=(board.P0_06, board.P1_13, board.P0_10),
                column_pins=(board.P0_11, board.P0_24,board.P1_06),
                columns_to_anodes=False,
            )
            self._encoder = rotaryio.IncrementalEncoder(board.P0_29, board.P0_31)

        elif 'BlueMicro840' in self._board_type:
            print("EncoderPad Pro with BlueMicro840")
            self._leds = LEDMatrix((board.P0_08,board.P0_02,board.P0_03),(board.P0_24,board.P0_20,board.P0_10),True)
            self._leds.reset_leds()
            self._speaker = Speaker(board.P0_29)

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
            self._speaker = Speaker(board.SPEAKER)

            self._keys = keypad.Keys((board.KEY1, board.KEY2, board.KEY3,
                                      board.KEY4, board.KEY5, board.KEY6,
                                      board.KEY7, board.KEY8, board.KEY8),
                                    value_when_pressed=False, pull=True)
            self._encoder = rotaryio.IncrementalEncoder(board.ROTA, board.ROTB)


    @property
    def keys(self):
        """
        The keys on the MacroPad. Uses events to track key number and state, e.g. pressed or
        released. You must fetch the events using ``keys.events.get()`` and then the events are
        available for usage in your code. Each event has three properties:
        * ``key_number``: the number of the key that changed. Keys are numbered starting at 0.
        * ``pressed``: ``True`` if the event is a transition from released to pressed.
        * ``released``: ``True`` if the event is a transition from pressed to released.
                        ``released`` is always the opposite of ``pressed``; it's provided
                        for convenience and clarity, in case you want to test for
                        key-release events explicitly.
        The following example prints the key press and release events to the serial console.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                key_event = macropad.keys.events.get()
                if key_event:
                    print(key_event)
        """
        return self._keys

    @property
    def encoder(self):
        """
        The rotary encoder relative rotation position. Always begins at 0 when the code is run, so
        the value returned is relative to the initial location.
        The following example prints the relative position to the serial console.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                print(macropad.encoder)
        """
        return self._encoder.position

    @property
    def speaker(self):
        return self._speaker

    @property
    def leds(self):
        return self._leds

    @property
    def pixels(self):
        """Sequence-like object representing the twelve NeoPixel LEDs in a 3 x 4 grid on the
        MacroPad. Each pixel is at a certain index in the sequence, numbered 0-11. Colors can be an
        RGB tuple like (255, 0, 0) where (R, G, B), or an RGB hex value like 0xFF0000 for red where
        each two digits are a color (0xRRGGBB). Set the global brightness using any number from 0
        to 1 to represent a percentage, i.e. 0.3 sets global brightness to 30%. Brightness defaults
        to 1.
        See ``neopixel.NeoPixel`` for more info.
        The following example turns all the pixels green at 50% brightness.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            macropad.pixels.brightness = 0.5
            while True:
                macropad.pixels.fill((0, 255, 0))
        The following example sets the first pixel red and the twelfth pixel blue.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                macropad.pixels[0] = (255, 0, 0)
                macropad.pixels[11] = (0, 0, 255)
        """
        return self._pixels

    @property
    def keyboard(self):
        """
        A keyboard object used to send HID reports. For details, see the ``Keyboard`` documentation
        in CircuitPython HID: https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html
        The following example types out the letter "a" when the rotary encoder switch is pressed.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                if macropad.encoder_switch:
                    macropad.keyboard.send(macropad.Keycode.A)
        """
        if self._keyboard is None:
            self._keyboard = Keyboard(usb_hid.devices)
        return self._keyboard

