import board
import keypad

# Define Keys
keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_30, board.P0_02, board.P0_29, board.P0_26),
    column_pins=(board.P0_06, board.P0_05, board.P0_08, board.P1_09, board.P0_04,
                 board.P0_12, board.P1_06, board.P0_24, board.P0_22, board.P0_13,
                 board.P0_15, board.P0_17, board.P0_20, board.P0_09, board.P0_10),
    columns_to_anodes=True,
)


while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
