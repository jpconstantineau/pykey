#pylint: disable = line-too-long
import time
import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keycode import PK_Keycode as KC

# define hardware
keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_30, board.P0_02, board.P0_29, board.P0_26),
    column_pins=(
        board.P0_06,
        board.P0_05,
        board.P0_08,
        board.P1_09,
        board.P0_04,
        board.P0_12,
        board.P1_06,
        board.P0_24,
        board.P0_22,
        board.P0_13,
        board.P0_15,
        board.P0_17,
        board.P0_20,
        board.P0_09,
        board.P0_10,
    ),
    columns_to_anodes=True,
)

# define keymap
layer = 0
keymap = (
        (
         KC.ESC ,     KC.ONE,   KC.TWO,   KC.THREE, KC.FOUR,  KC.FIVE,  KC.SIX,   KC.SEVEN,  KC.EIGHT,    KC.NINE,   KC.ZERO,     KC.MINUS,     KC.EQUALS ,     KC.BSPACE ,     KC.BSPACE ,
         KC.TAB,     KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,      KC.I,        KC.O,      KC.P,        KC.LEFT_BRACKET ,  KC.RIGHT_BRACKET ,  KC.BACKSLASH ,     KC.PAGE_UP ,
         KC.CAPS_LOCK ,    KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,      KC.K,        KC.L,      KC.SCOLON,   KC.QUOTE,     KC.ENTER,     KC.ENTER,      KC.PAGE_DOWN ,
         KC.LEFT_SHIFT ,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,      KC.COMMA,    KC.DOT,    KC.SLASH,    KC.RSHIFT,    KC.RSHIFT,    KC.UP_ARROW ,         KC.NO,
         KC.LEFT_CONTROL ,   KC.LEFT_CONTROL, KC.LEFT_GUI ,  KC.LEFT_ALT ,  KC.SPACE,   KC.SPACE,   KC.SPACE,   KC.SPACE,    KC.SPACE,      KC.RIGHT_CONTROL ,  KC.RIGHT_ALT ,
         KC.RIGHT_GUI ,   KC.LEFT_ARROW ,      KC.DOWN_ARROW ,       KC.RIGHT_ARROW
         ),
         (
         KC.ESCAPE ,     KC.ONE,   KC.TWO,   KC.THREE, KC.FOUR,  KC.FIVE,  KC.SIX,   KC.SEVEN,  KC.EIGHT,    KC.NINE,   KC.ZERO,     KC.MINUS,     KC.EQUALS ,     KC.BSPACE ,     KC.BSPACE ,
         KC.TAB,     KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,      KC.I,        KC.O,      KC.P,        KC.LEFT_BRACKET ,  KC.RIGHT_BRACKET ,  KC.BACKSLASH ,     KC.PAGE_UP ,
         KC.CAPS_LOCK ,    KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,      KC.K,        KC.L,      KC.SCOLON,   KC.QUOTE,     KC.ENTER,     KC.ENTER,      KC.PAGE_DOWN ,
         KC.LEFT_SHIFT ,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,      KC.COMMA,    KC.DOT,    KC.SLASH,    KC.RSHIFT,    KC.RSHIFT,    KC.UP_ARROW ,         KC.NO,
         KC.LEFT_CONTROL ,   KC.LEFT_CONTROL, KC.LEFT_GUI ,  KC.LEFT_ALT ,  KC.SPACE,   KC.SPACE,   KC.SPACE,   KC.SPACE,    KC.SPACE,      KC.RIGHT_CONTROL ,  KC.RIGHT_ALT ,
         KC.RIGHT_GUI ,   KC.LEFT_ARROW ,      KC.DOWN_ARROW ,       KC.RIGHT_ARROW
         )
)


# setup variables
not_sleeping = True

keyboard = Keyboard(usb_hid.devices)

while not_sleeping:
    key_event = keys.events.get()
    if key_event:
        key = keymap[layer][key_event.key_number]
        if key_event.pressed:
            keyboard.press(key)
        else:
            keyboard.release(key)

    time.sleep(0.002)
