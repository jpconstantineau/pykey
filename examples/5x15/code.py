import board
import keypad

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
keymap = ((
    "ESC", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "DELETE", "BSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "PGUP",   "UP",
    "CAPS","A", "S", "D", "F", "G", "H", "J", "K", "L", ";", '"', "ENTER", "PGDN", "DOWN",
    "LSHIFT", "Z","X","C","V", "B", "N", "M", ",", ".", "/", "RSHIFT","LEFT","UP","RIGHT",
    "LCTL","FN","META","LALT","LOWER","SPACE","SPACE","SPACE","SPACE","RAISE","RGUI","RCTL","LEFT","DOWN","RIGHT"
),
(
    "ESC", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "DELETE", "BSPACE",
    "TAB", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "PGUP",   "UP",
    "CAPS","A", "S", "D", "F", "G", "H", "J", "K", "L", ";", '"', "ENTER", "PGDN", "DOWN",
    "LSHIFT", "Z","X","C","V", "B", "N", "M", ",", ".", "/", "RSHIFT","LEFT","UP","RIGHT",
    "LCTL","FN","META","LALT","LOWER","SPACE","SPACE","SPACE","SPACE","RAISE","RGUI","RCTL","LEFT","DOWN","RIGHT"
))


# setup variables
keylist = []

while True:
    key_event = keys.events.get()
    if key_event:
        if key_event.pressed:
            keylist.append(key_event.key_number)
        else:
            keylist.remove(key_event.key_number)
        if len(keylist) > 0:
            print(keymap[layer][keylist[0]])
