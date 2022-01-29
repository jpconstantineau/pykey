from adafruit_hid.keycode import Keycode as KC # REQUIRED if using KC.* values
from adafruit_hid.mouse import Mouse
from adafruit_hid.consumer_control_code import ConsumerControlCode
#https://circuitpython.readthedocs.io/projects/hid/en/latest/_modules/adafruit_hid/keycode.html

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'iTunes', # Application name
    'encoder' : [ (0x000000, 'Vol-', [[ConsumerControlCode.VOLUME_DECREMENT]]),
                  (0x000000, 'Vol+', [[ConsumerControlCode.VOLUME_INCREMENT]])
    ],
    'macros' : [           # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        (0x202020, '', [   ]),
        (0x000000, '', [   ]),
        (0x200020, 'previous', [ KC.LEFT_ARROW ]),
        (0x200020, 'back', [KC.LEFT_CONTROL, KC.LEFT_ALT, KC.LEFT_ARROW  ]),
        (0x200020, 'play/pause', [ KC.SPACE  ]),
        (0x200020, 'forward', [KC.LEFT_CONTROL, KC.LEFT_ALT, KC.RIGHT_ARROW  ]),
        (0x200020, 'next', [ KC.RIGHT_ARROW  ]),
        (0x002000, 'Mute', [[ConsumerControlCode.MUTE]]),
        (0x000000, '', [   ]),
    ]
}
