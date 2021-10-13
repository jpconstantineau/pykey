# Note: Certain keys may not be fully supported by the adafruit_hid module. You can work around this:

# If you absolutely must have an unsupported character then you may replace the Key Sequence for that key with something that follows the pattern of:
# [ "Example Character" ] be aware that this key will only do this character or sequence of characters...it will not change when you hold down'Shift' or 'Control'

# If you need the key to type a sentence then you may replace the Key Sequence for that key with something that follows the pattern of:
# ["Example sentence"]

# If you need the key to enter two different keys at the same time then you may replace the Key Sequence for that Key with something that follows the pattern of:
# [ KC.LEFT_CONTROL, KC.C ] (this would make it a copy button)  Please note that in this example the order of the key presses may matter.

# If you find yourself trying to enter a complex series of key presses and find that the keyboard continues to press KC.LEFT_CONTROL, for instance, you may want to
# replace the Key Sequence for that Key with something that follows the pattern of:
# [ KC.LEFT_CONTROL, -KC.LEFT_CONTROL ]  (note the placement of the '-' to designate that you wish to stop pressing that key)

# To see the full list of supported KB_Kecode characters type in the CircuitPython REPL:
#>>> from pykey.keycode import KB_Keycode
#>>> print(dir(KB_Keycode))

from pykey.keycode import PK_Keycode as KC # REQUIRED if using KC.* values

layer = {                    # REQUIRED dict, must be named 'layer'
    'name' : 'Layer 1', # Application name
    'macros' : [           # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row - top row ----------
        (0x202000, 'ESC', [ KC.ESC ]),
        (0x202000, '1', [ KC.ONE ]),
        (0x202000, '2', [ KC.TWO ]),
        (0x202000, '3', [ KC.THREE ]),
        (0x202000, '4', [ KC.FOUR ]),
        (0x202000, '5', [ KC.FIVE ]),
        (0x202000, '6', [ KC.SIX ]),
        (0x202000, '7', [ KC.SEVEN ]),
        (0x202000, '8', [ KC.EIGHT ]),
        (0x202000, '9', [ KC.NINE ]),
        (0x800000, '0', [ KC.ZERO ]),
        (0x202000, '-', [KC.MINUS]),
        (0x202000, '=', [KC.EQUALS]),
        (0x202000, 'BS', [KC.BSPACE]),
        # 2nd row ----------
        (0x202000, 'TAB', [ KC.TAB ]),
        (0x202000, 'q', [ KC.Q ]),
        (0x202000, 'w', [ KC.W ]),
        (0x202000, 'e', [ KC.E ]),
        (0x202000, 'r', [ KC.R ]),
        (0x202000, 't', [ KC.T ]),
        (0x202000, 'y', [ KC.Y ]),
        (0x202000, 'u', [ KC.U ]),
        (0x202000, 'i', [ KC.I ]),
        (0x202000, 'o', [ KC.O ]),
        (0x800000, 'p', [ KC.P ]),
        (0x202000, '[', [KC.LEFT_BRACKET]),
        (0x202000, ']', [KC.RIGHT_BRACKET]),
        (0x202000, '\\', [KC.BACKSLASH]),
        # 3rd row ----------
        (0x202000, 'CAPS', [ KC.CAPS_LOCK ]),
        (0x202000, 'a', [ KC.A ]),
        (0x202000, 's', [ KC.S ]),
        (0x202000, 'd', [ KC.D ]),
        (0x202000, 'f', [ KC.F ]),
        (0x202000, 'g', [ KC.G ]),
        (0x202000, 'h', [ KC.H ]),
        (0x202000, 'j', [ KC.J ]),
        (0x202000, 'k', [ KC.K ]),
        (0x202000, 'l', [ KC.L ]),
        (0x800000, ';', [ KC.SCOLON ]),
        (0x202000, '\'', [KC.QUOTE]),
        (0x202000, 'ENT', [KC.ENTER]),
        (0x202000, 'ENT', [KC.ENTER]),
        # 4th row ----------
        (0x202000, 'LSHFT', [ KC.LEFT_SHIFT ]),
        (0x202000, 'z', [ KC.Z ]),
        (0x202000, 'x', [ KC.X ]),
        (0x202000, 'c', [ KC.C ]),
        (0x202000, 'v', [ KC.V ]),
        (0x202000, 'b', [ KC.B ]),
        (0x202000, 'n', [ KC.N ]),
        (0x202000, 'm', [ KC.M ]),
        (0x202000, ',', [ KC.COMMA ]),
        (0x202000, '.', [ KC.DOT ]),
        (0x800000, '/', [ KC.SLASH ]),
        (0x202000, 'RSHFT', [KC.RSHIFT]),
        (0x202000, 'RSHFT', [KC.RSHIFT]),
        (0x202000, 'NO', [KC.NO]),
        # 5th row - bottom row ----------
        (0x800000, '0', [ KC.LEFT_CONTROL ]),
        (0x101010, 'L1', [ KC.LAYER_1 ]),
        (0x101010, 'LGUI', [ KC.LEFT_GUI ]),
        (0x800000, 'LALT', [ KC.LEFT_ALT ]),
        (0x101010, 'L1', [ KC.LAYER_1 ]),
        (0x101010, 'SPC', [ KC.SPACE ]),
        (0x101010, 'SPC', [ KC.SPACE ]),
        (0x101010, 'SPC', [ KC.SPACE ]),
        (0x101010, 'SPC', [ KC.SPACE ]),
        (0x101010, 'RCTL', [ KC.RIGHT_CONTROL ]),
        (0x101010, 'RALT', [ KC.RIGHT_ALT ]),
        (0x101010, 'RGUI', [ KC.RIGHT_GUI ]),
        (0x800000, 'left', [ KC.LEFT_ARROW ]),
        (0x101010, 'down', [ KC.DOWN_ARROW ]),

    ]
}
