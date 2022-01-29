# MACROPAD Hotkeys example: Universal Numpad

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                    # REQUIRED dict, must be named 'app'
    'name' : 'Num2', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE

        (0x202000, 'NumLock', ['a']),
        (0x202000, '/', ['/']),
        (0x202000, '*', ['*']),
        (0x202000, 'd', ['d']),#encoder button
        (0x202000, '7', ['7']),
        (0x202000, '8', ['8']),
        (0x202000, '9', ['9']),
        # 2nd row ----------
        (0x202000, '-', ['-']),#top row right
        (0x202000, '4', ['4']),
        (0x202000, '5', ['5']),
        (0x202000, '6', ['6']),
        # 3rd row ----------
        (0x202000, '+', ['+']),# +
        (0x202000, '1', ['1']),
        (0x202000, '2', ['2']),
        (0x202000, '3', ['3']),
        # 4th row ----------
        (0x101010, 'enter', ['e']),
        (0x800000, '0', ['0']),
        (0x101010, '#', ['#']),#empty
        (0x101010, '.', ['.']),
        (0x101010, '.', ['.']),
    ]
}
