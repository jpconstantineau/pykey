from pykey.keycode import KB_Keycode as KC  # REQUIRED if using KC.* values

layer = {  # REQUIRED dict, must be named 'layer'
    "name": "Layer 0",  # Application name
    "macros": [  # keys ...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row - top row ----------
        (0x202000, "q", [KC.Q]),
        (0x202000, "w", [KC.W]),
        (0x202000, "e", [KC.E]),
        (0x202000, "r", [KC.R]),
        (0x202000, "t", [KC.T]),
        (0x202000, "Grave", [KC.GRAVE_ACCENT]),
        (0x202000, "y", [KC.Y]),
        (0x202000, "u", [KC.U]),
        (0x202000, "i", [KC.I]),
        (0x202000, "o", [KC.O]),
        (0x800000, "p", [KC.P]),
        # 2nd row ----------
        (0x202000, "a", [KC.A]),
        (0x202000, "s", [KC.S]),
        (0x202000, "d", [KC.D]),
        (0x202000, "f", [KC.F]),
        (0x202000, "g", [KC.G]),
        (0x202000, "LEFT_CONTROL", [KC.LEFT_CONTROL]),
        (0x202000, "h", [KC.H]),
        (0x202000, "j", [KC.J]),
        (0x202000, "k", [KC.K]),
        (0x202000, "l", [KC.L]),
        (0x800000, ";", [KC.SCOLON]),
        # 3rd row ----------
        (0x202000, "z", [KC.Z]),
        (0x202000, "x", [KC.X]),
        (0x202000, "c", [KC.C]),
        (0x202000, "v", [KC.V]),
        (0x202000, "b", [KC.B]),
        (0x202000, "\|", [KC.BACKSLASH]),
        (0x202000, "n", [KC.N]),
        (0x202000, "m", [KC.M]),
        (0x202000, ",", [KC.COMMA]),
        (0x202000, ".", [KC.DOT]),
        (0x800000, "/", [KC.SLASH]),
        # 4th row ----------
        (0x202000, "ESCAPE ", [KC.ESCAPE]),
        (0x202000, "TAB", [KC.TAB]),
        (0x202000, "LEFT_GUI", [KC.LEFT_GUI]),
        (0x202000, "LEFT_SHIFT ", [KC.LEFT_SHIFT]),
        (0x202000, "BACKSPACE", [KC.BACKSPACE]),
        (0x202000, "LEFT_ALT ", [KC.LEFT_ALT]),
        (0x202000, "SPACE", [KC.SPACE]),
        (0x202000, "FUN", [KC.DOT]),
        (0x202000, "MINUS ", [KC.MINUS]),
        (0x202000, "QUOTE ", [KC.QUOTE]),
        (0x202000, "ENTER", [KC.ENTER]),
    ],
}
