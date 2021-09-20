import keypad
import board
import usb_hid
from pykey.BitmapKeyboard import BitmapKeyboard
from pykey.keycode import PK_Keycode as Keycode

key_pins = (
    board.KEY1,
    board.KEY2,
    board.KEY3,
    board.KEY4,
    board.KEY5,
    board.KEY6,
    board.KEY7,
    board.KEY8,
    board.KEY9,
    board.KEY10,
    board.KEY11,
    board.KEY12,
)

keys = keypad.Keys(key_pins, value_when_pressed=False, pull=True)

kbd = BitmapKeyboard(usb_hid.devices)

keymap = [
    Keycode.ONE, Keycode.TWO, Keycode.THREE,
    Keycode.Q, Keycode.W, Keycode.E,
    Keycode.A, Keycode.S, Keycode.D,
    Keycode.Z, Keycode.X, Keycode.C]

while True:
    ev = keys.events.get()
    if ev is not None:
        key = keymap[ev.key_number]
        if ev.pressed:
            kbd.press(key)
        else:
            kbd.release(key)
