from adafruit_hid.keycode import Keycode as KC # REQUIRED if using KC.* values

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'Layer 0', # Application name
    'encoder' : [ (0x202000, 'LEFT', [ KC.LEFT_ARROW ]),
                  (0x202000, 'RIGHT',[ KC.RIGHT_ARROW ])
    ],
    'macros' : [           # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        (0x202000, '1', [ KC.ONE ]),
        (0x202000, '2', [ KC.TWO ]),
        (0x202000, '3', [ KC.THREE ]),
        (0x202000, '4', [ KC.FOUR ]),
        (0x101010, '5', [ KC.FIVE ]),
        (0x202000, '6', [ KC.SIX ]),
        (0x202000, '7', [ KC.SEVEN ]),
        (0x202000, '8', [ KC.EIGHT ]),
        (0x101010, '9', [ KC.NINE ])
    ]
}
