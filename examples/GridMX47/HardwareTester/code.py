import time
import board
import neopixel
import rainbowio
import pwmio
import keypad
from digitalio import DigitalInOut, Direction
# the following assumes that RP Pico is the board flashed to it...
# define audio hardware
buzzer = pwmio.PWMOut(board.GP3, variable_frequency=True)
OFF = 0
ON = 2**15
buzzer.frequency = 1660 #
# Hardware definition: GPIO where RGB LED is connected.
pixel_pin = board.GP6
num_pixels = 65

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

led1 = DigitalInOut(board.LED)
led1.direction = Direction.OUTPUT

def rainbow_cycle(number):

        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) +number
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()


# Switch Matrix Setup.
keys = keypad.KeyMatrix(
            row_pins=(board.GP7, board.GP8, board.GP9, board.GP10),
            column_pins=(board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP19, board.GP20,
                        board.GP21, board.GP22, board.GP26, board.GP27, board.GP28),
            columns_to_anodes=True,
        )

i = 0
while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            buzzer.duty_cycle = ON
            led1.value = True
        else:
            buzzer.duty_cycle = OFF
            led1.value = False
    else:
        i = i+1
        rainbow_cycle(i)
