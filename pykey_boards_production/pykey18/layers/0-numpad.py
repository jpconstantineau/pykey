# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE

        (0x202000, 'a', [Keycode.KEYPAD_NUMLOCK]),
        (0x202000, '/', [Keycode.KEYPAD_FORWARD_SLASH]),
        (0x202000, '*', [Keycode.KEYPAD_ASTERISK]),
        (0x202000, 'hello', ['hello']),#encoder button
        (0x202000, '7', [Keycode.KEYPAD_SEVEN]),
        (0x202000, '8', [Keycode.KEYPAD_EIGHT]),
        (0x202000, '9', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x202000, '-', [Keycode.KEYPAD_MINUS]),#top row right
        (0x202000, '4', [Keycode.KEYPAD_FOUR]),
        (0x202000, '5', [Keycode.KEYPAD_FIVE]),
        (0x202000, '6', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x202000, '+', [Keycode.KEYPAD_PLUS]),# +
        (0x202000, '1', [Keycode.KEYPAD_ONE]),
        (0x202000, '2', [Keycode.KEYPAD_TWO]),
        (0x202000, '3', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x101010, 'enter', [Keycode.KEYPAD_ENTER]),
        (0x800000, '0', [Keycode.KEYPAD_ZERO]),
        (0x101010, '#', ['#']),#empty
        (0x101010, '.', [Keycode.KEYPAD_PERIOD]),
        (0x101010, '.', ['.']),#empty
    ]
}
