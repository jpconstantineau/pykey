import time
import board
import neopixel
import rainbowio
import pwmio
import keypad
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import rotaryio

from digitalio import DigitalInOut, Direction



# LED setup.
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.ENCA, board.ENCB)
last_position = None
displayio.release_displays()


#i2c = busio.I2C(board.SCL, board.SDA)
#display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
BORDER = 5

#display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)



# the following assumes that RP Pico is the board flashed to it...
# define audio hardware
buzzer = pwmio.PWMOut(board.SPEAKER, variable_frequency=True)
OFF = 0
ON = 2**15
buzzer.frequency = 1660 #
# Hardware definition: GPIO where RGB LED is connected.
pixel_pin = board.NEOPIXEL
num_pixels = 18

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

def rainbow_cycle(number):

        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) +number
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()


# Switch Matrix Setup.
keys = keypad.KeyMatrix(
            row_pins=(board.ROW1, board.ROW2, board.ROW3, board.ROW4, board.ROW5),
            column_pins=(board.COL1, board.COL2, board.COL3, board.COL4,
                        ),
            columns_to_anodes=True,
        )

i = 0
while True:
    #splash = displayio.Group()
    #display.show(splash)
    key_event = keys.events.get()
    if key_event:
        print(key_event)
        if key_event.pressed:
            buzzer.duty_cycle = ON
            led.value = True
        else:
            buzzer.duty_cycle = OFF
            led.value = False
    else:
        i = i+1
        rainbow_cycle(i)
    position = encoder.position
    if last_position is None or position != last_position:
        print(position)
    last_position = position
