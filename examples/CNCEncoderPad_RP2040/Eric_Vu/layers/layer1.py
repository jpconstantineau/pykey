from adafruit_hid.keycode import Keycode as KC # REQUIRED if using KC.* values
from adafruit_hid.mouse import Mouse

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'Layer 1', # Application name
    'encoder' : [ (0x202020, 'Down', [{'wheel':1}]),
                  (0x202020, 'Up', [{'wheel':-1}])
    ],
    'macros' : [           # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        (0x202020, '1', [   ]),
        (0x002000, '2', [ KC.LEFT_GUI, KC.LEFT_ALT, KC.PRINT_SCREEN ]),
        (0x000020, '3', [ KC.DOWN_ARROW ]),
        (0x200000, '4', [ KC.UP_ARROW  ]),
        (0x002000, '5', [ KC.RIGHT_ARROW  ]),
        (0x000020, '6', [ KC.LEFT_ARROW  ]),
        (0x200000, 'cut', [KC.CONTROL, 'x']),
        (0x002000, 'copy', [KC.CONTROL, 'c']),
        (0x000020, 'paste', [KC.CONTROL, 'v']),
    ]
}
