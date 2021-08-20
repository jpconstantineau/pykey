import board
import keypad

# Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.ROW0, board.ROW1, board.ROW2, board.ROW3),
    column_pins=(board.COL0, board.COL1, board.COL2, board.COL3,board.COL4, board.COL5, board.COL6, board.COL7),
    columns_to_anodes=False,
)


while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)