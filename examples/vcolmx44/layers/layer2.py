from pykey.keycode import KB_Keycode as KC  # REQUIRED if using KC.* values

layer = {  # REQUIRED dict, must be named 'layer'
    "name": "Layer 2",  # Application name
    "macros": [  # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row - top row ----------
        (0x202000, "INS", [KC.INSERT]),
        (0x202000, "HOME", [KC.HOME]),
        (0x202000, "UP", [KC.UP_ARROW]),
        (0x202000, "END", [KC.END]),
        (0x202000, "PgUp", [KC.PAGE_UP]),
        (0x202000, "^", [KC.LEFT_SHIFT, KC.SIX]),
        (0x202000, "Up", [KC.UP_ARROW]),
        (0x202000, "F7", [KC.F7]),
        (0x202000, "F8", [KC.F8]),
        (0x202000, "F9", [KC.F9]),
        (0x800000, "F10", [KC.F10]),
        # 2nd row ----------
        (0x202000, "DEL", [KC.DELETE]),
        (0x202000, "LEFT", [KC.LEFT_ARROW]),
        (0x202000, "DOWN", [KC.DOWN_ARROW]),
        (0x202000, "RIGHT", [KC.RIGHT_ARROW]),
        (0x202000, "PgDn", [KC.PAGE_DOWN]),
        (0x202000, "NO", [KC.LEFT_CONTROL]),
        (0x202000, "Dn", [KC.DOWN_ARROW]),
        (0x202000, "F4", [KC.F4]),
        (0x202000, "F5", [KC.F5]),
        (0x202000, "F6", [KC.F6]),
        (0x800000, "F11", [KC.F11]),
        # 3rd row ----------
        (0x202000, "NO", [KC.LEFT_BRACKET]),
        (0x202000, "VOLU", [KC.RIGHT_BRACKET]),
        (0x202000, "NO", [KC.LEFT_SHIFT, KC.THREE]),
        (0x202000, "NO", [KC.LEFT_SHIFT, KC.LEFT_BRACKET]),
        (0x202000, "NO", [KC.LEFT_SHIFT, KC.RIGHT_BRACKET]),
        (0x202000, "TRNS", [KC.LEFT_SHIFT, KC.SEVEN]),
        (0x202000, "NO", [KC.LEFT_SHIFT, KC.EIGHT]),
        (0x202000, "F1", [KC.F1]),
        (0x202000, "F2", [KC.F2]),
        (0x202000, "F3", [KC.F3]),
        (0x800000, "F12", [KC.F12]),
        # 4th row ----------
        (0x202000, "NO", [KC.ESCAPE]),
        (0x202000, "VOLD", [KC.INSERT]),
        (0x202000, "LEFT_GUI", [KC.LEFT_GUI]),
        (0x202000, "LEFT_SHIFT ", [KC.LEFT_SHIFT]),
        (0x202000, "BACKSPACE", [KC.BACKSPACE]),
        (0x202000, "LEFT_ALT ", [KC.LEFT_ALT]),
        (0x202000, "SPACE", [KC.SPACE]),
        (0x202000, "FUN", [KC.DOT]),
        (0x202000, "PRTSCR", [KC.PRINT_SCREEN]),
        (0x202000, "SCRLCK", [KC.SCROLL_LOCK]),
        (0x202000, "PAUS", [KC.PAUSE]),
    ],
}
