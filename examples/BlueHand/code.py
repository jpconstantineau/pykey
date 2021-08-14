#pylint: disable = line-too-long
import board
import keypad
import pwmio
import time

# define audio hardware
buzzer = pwmio.PWMOut(board.P1_13, variable_frequency=True)
OFF = 0
ON = 2**15
not_sleeping = True

# define key GPIOs
keys = keypad.Keys(pins=(board.P0_29,board.P0_02,board.P0_28,board.P0_03,board.P0_10,board.P0_09,board.P0_24,board.P0_13),value_when_pressed=False)


# End of Setup Music
buzzer.duty_cycle = ON
buzzer.frequency = 440
time.sleep(0.05)
buzzer.frequency = 880
time.sleep(0.05)
buzzer.frequency = 440
time.sleep(0.05)
buzzer.duty_cycle = OFF

while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)