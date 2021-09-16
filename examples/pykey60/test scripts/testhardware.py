import time
import board
import neopixel
import rainbowio
import pwmio
import keypad
# the following assumes that RP Pico is the board flashed to it...
# define audio hardware
buzzer = pwmio.PWMOut(board.GP21, variable_frequency=True)
OFF = 0
ON = 2**15
buzzer.frequency = 1660 # 
# Hardware definition: GPIO where RGB LED is connected. 
pixel_pin = board.A3
num_pixels = 65

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

def rainbow_cycle(number):

        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) 
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
            if i == number:
                pixels[i] = (101, 47, 143) #blinka purple
        pixels.show()


# Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.GP14, board.GP15, board.GP16, board.GP17, board.GP18),
    column_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6,
                 board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13),
    columns_to_anodes=True,
)


while True:
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            buzzer.duty_cycle = ON
        else:
            buzzer.duty_cycle = OFF
        rainbow_cycle(key_event.key_number) 