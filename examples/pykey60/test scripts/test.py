import board
from digitalio import DigitalInOut, Direction
import time

# LED setup.
led = DigitalInOut(board.GP24)
led.direction = Direction.OUTPUT

import board
import time



# define audio hardware
buzzer = pwmio.PWMOut(board.GP21, variable_frequency=True)
OFF = 0
ON = 2**15
not_sleeping = True


# End of Setup Music
buzzer.duty_cycle = ON
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.frequency = 880 # 
time.sleep(0.05)
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.duty_cycle = OFF


while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)