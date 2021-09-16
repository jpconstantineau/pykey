import board
import keypad

# Switch Matrix Setup.
keys = keypad.KeyMatrix(
    column_pins=(board.GP14, board.GP15, board.GP16, board.GP17, board.GP18),
    row_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
                 board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13),
    columns_to_anodes=False,
)


while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
