import board
import rotaryio


# define hardware

encoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_06)
last_position = None

# define keymaps

# call loop

while True:
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position