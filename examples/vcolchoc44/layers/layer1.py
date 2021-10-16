from pykey.keycode import KB_Keycode as KC  # REQUIRED if using KC.* values

layer = {  # REQUIRED dict, must be named 'layer'
    "name": "Layer 1",  # Application name
    "macros": [  # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row - top row ----------
        (0x202000, "!", [KC.LEFT_SHIFT, KC.ONE]),
        (0x202000, "@", [KC.LEFT_SHIFT, KC.TWO]),
        (0x202000, "UP", [KC.UP_ARROW]),
        (0x202000, "$", [KC.LEFT_SHIFT, KC.FOUR]),
        (0x202000, "%", [KC.LEFT_SHIFT, KC.FIVE]),
        (0x202000, "^", [KC.LEFT_SHIFT, KC.SIX]),
        (0x202000, "PgUp", [KC.PAGE_UP]),
        (0x202000, "7", [KC.SEVEN]),
        (0x202000, "8", [KC.EIGHT]),
        (0x202000, "9", [KC.NINE]),
        (0x800000, "BACKSPACE", [KC.BACKSPACE]),
        # 2nd row ----------
        (0x202000, "(", [KC.LEFT_SHIFT, KC.NINE]),
        (0x202000, "LEFT", [KC.LEFT_ARROW]),
        (0x202000, "DOWN", [KC.DOWN_ARROW]),
        (0x202000, "RIGHT", [KC.RIGHT_ARROW]),
        (0x202000, ")", [KC.LEFT_SHIFT, KC.ZERO]),
        (0x202000, "NO", [KC.LEFT_CONTROL]),
        (0x202000, "PgDn", [KC.PAGE_DOWN]),
        (0x202000, "4", [KC.FOUR]),
        (0x202000, "5", [KC.FIVE]),
        (0x202000, "6", [KC.SIX]),
        (0x800000, "NO", [KC.SCOLON]),
        # 3rd row ----------
        (0x202000, "[", [KC.LEFT_BRACKET]),
        (0x202000, "]", [KC.RIGHT_BRACKET]),
        (0x202000, "#", [KC.LEFT_SHIFT, KC.THREE]),
        (0x202000, "{", [KC.LEFT_SHIFT, KC.LEFT_BRACKET]),
        (0x202000, "}", [KC.LEFT_SHIFT, KC.RIGHT_BRACKET]),
        (0x202000, "&", [KC.LEFT_SHIFT, KC.SEVEN]),
        (0x202000, "*", [KC.LEFT_SHIFT, KC.EIGHT]),
        (0x202000, "1", [KC.ONE]),
        (0x202000, "2", [KC.TWO]),
        (0x202000, "3", [KC.THREE]),
        (0x800000, "+", [KC.LEFT_SHIFT, KC.EQUALS]),
        # 4th row ----------
        (0x202000, "LAYER 2 ", [KC.ESCAPE]),
        (0x202000, "INS", [KC.INSERT]),
        (0x202000, "LEFT_GUI", [KC.LEFT_GUI]),
        (0x202000, "LEFT_SHIFT ", [KC.LEFT_SHIFT]),
        (0x202000, "BACKSPACE", [KC.BACKSPACE]),
        (0x202000, "LEFT_ALT ", [KC.LEFT_ALT]),
        (0x202000, "SPACE", [KC.SPACE]),
        (0x202000, "FUN", [KC.DOT]),
        (0x202000, ". ", [KC.DOT]),
        (0x202000, "0 ", [KC.ZERO]),
        (0x202000, "EQUALS", [KC.EQUALS]),
    ],
}
