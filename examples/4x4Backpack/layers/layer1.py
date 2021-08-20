from keycode import PK_Keycode as KC # REQUIRED if using KC.* values

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'layer 1', # Application name
    'macros' : [           # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x202000, '7', [ KC.A ]),
        (0x202000, '8', [ KC.B ]),
        (0x202000, '9', [ KC.C ]),
        (0x202000, '-', [ KC.D ]),
        # 2nd row ----------
        (0x202000, '4', [ KC.E ]),
        (0x202000, '5', [ KC.F ]),
        (0x202000, '6', [ KC.G ]),
        (0x202000, '+', ['+']),
        # 3rd row ----------
        (0x202000, '1', [ KC.H ]),
        (0x202000, '2', [ KC.I ]),
        (0x202000, '3', [ KC.J ]),
        (0x202000, '/', ['/']),
        # 4th row ----------
        (0x101010, '*', [ KC.LAYER_1 ]),
        (0x800000, '0', [ KC.ZERO ]),
        (0x101010, '#', [ KC.SEVEN, KC.SHIFT ]),
        (0x202000, '*', ['Hello World'])
    ]
}
