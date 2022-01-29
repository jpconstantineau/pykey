from adafruit_hid.keycode import Keycode as KC # REQUIRED if using KC.* values
# To reference Consumer Control codes, import ConsumerControlCode like so...
from adafruit_hid.consumer_control_code import ConsumerControlCode
#https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'Layer 0', # Application name
    'encoder' : [ (0x000000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
                  (0x000000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]])
    ],
    'macros' : [           # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        (0x202020, '1', [   ]),
        (0x000020, '2', [ KC.TWO ]),
        (0x000020, '3', [ KC.DOWN_ARROW ]),
        (0x000020, '4', [ KC.UP_ARROW  ]),
        (0x000020, '5', [ KC.RIGHT_ARROW  ]),
        (0x000020, '6', [ KC.LEFT_ARROW  ]),
        (0x000020, 'cut', [KC.CONTROL, 'x']),
        (0x000020, 'copy', [KC.CONTROL, 'c']),
        (0x000020, 'paste', [KC.CONTROL, 'v']),
    ]
}
