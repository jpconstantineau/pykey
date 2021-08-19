from adafruit_hid.keycode import Keycode as KC # REQUIRED if using Keycode.* values

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'Numpad', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', [ KC.SEVEN ]),
        (0x202000, '8', [ KC.EIGHT ]),
        (0x202000, '9', [ KC.NINE ]),
        (0x202000, '-', [ KC.MINUS ]),
        # 2nd row ----------
        (0x202000, '4', [ KC.FOUR ]),
        (0x202000, '5', [ KC.FIVE ]),
        (0x202000, '6', [ KC.SIX ]),
        (0x202000, '+', ['+']),
        # 3rd row ----------
        (0x202000, '1', [ KC.ONE ]),
        (0x202000, '2', [ KC.TWO ]),
        (0x202000, '3', [ KC.THREE ]),
        (0x202000, '/', ['/']),
        # 4th row ----------
        (0x101010, '*', ['*']),
        (0x800000, '0', [ KC.ZERO ]),
        (0x101010, '#', [ KC.SEVEN, KC.SHIFT ]),
        (0x202000, '*', ['Hello World'])
    ]
}
