
# pylint: disable=import-error, unused-import, too-few-public-methods
import board
import os
import rotaryio
import busio
import displayio
import terminalio
import keypad
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_display_text import label
from adafruit_display_text import label
import adafruit_displayio_ssd1306

# Hardware definition: GPIO where RGB LED is connected.
pixel_pin = board.NEOPIXEL
num_pixels = 18  # adding 1 to make sure we have a place for the empty spots
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.4, auto_write=False)

# Encoder Setup
encoder = rotaryio.IncrementalEncoder(board.ENCA, board.ENCB)
last_position = None

displayio.release_displays()
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

WIDTH = 128
HEIGHT = 32  # Change to 64 if needed
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=WIDTH, height=HEIGHT)

keys = keypad.KeyMatrix(
            row_pins=(board.ROW1, board.ROW2, board.ROW3, board.ROW4, board.ROW5),
            column_pins=(board.COL1, board.COL2, board.COL3, board.COL4,
                        ),
            columns_to_anodes=True,
        )

key_to_pixel = [0, 1,2,17,4,5,6,3,7,8,9,10,11,12,13,14,15,16,16,17,17,17] # 17 is a dummy spot
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'


# CLASSES AND FUNCTIONS ----------------

class App:
    """ Class representing a host-side application, for which we have a set
        of macro sequences. Project code was originally more complex and
        this was helpful, but maybe it's excessive now?"""
    def __init__(self, appdata):
        self.name = appdata['name']
        self.macros = appdata['macros']

    def switch(self):
        """ Activate application settings; update OLED labels and LED
            colors. """
        group[0].text = self.name   # Application name
        for i in range(len(self.macros)):
            pixels[key_to_pixel[i]] = self.macros[i][0]
        keyboard.release_all()
        pixels.show()
        display.refresh()


# INITIALIZATION -----------------------

display.auto_refresh = False
pixels.auto_write = False

# Set up displayio group with all the labels
group = displayio.Group()
group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                         anchored_position=(display.width//2, -2),
                         anchor_point=(0.5, 0.0)))
group.append(label.Label(terminalio.FONT, text='', color=0xFFFFFF,
                         anchored_position=(display.width//2, 10),
                         anchor_point=(0.5, 0.0)))
display.show(group)

# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.app))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            pass

if not apps:
    group[0].text = 'NO MACRO FILES FOUND'
    display.refresh()
    while True:
        pass

last_position = None
app_index = 0
apps[app_index].switch()


# MAIN LOOP ----------------------------

while True:
    # Read encoder position. If it's changed, switch layer.
    position = encoder.position
    if position != last_position:
        app_index = position % len(apps)
        apps[app_index].switch()
        last_position = position

    event = keys.events.get()
    if not event or event.key_number >= len(apps[app_index].macros):
        continue # No key events, or no corresponding macro, resume loop
    key_number = event.key_number
    pressed = event.pressed

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

    sequence = apps[app_index].macros[key_number][2]
    if pressed:
        pixels[key_to_pixel[key_number]] = 0xFFFFFF
        pixels.show()
        group[1].text = apps[app_index].macros[key_number][1]
        display.refresh()
        for item in sequence:
            if isinstance(item, int):
                if item >= 0:
                    keyboard.press(item)
                else:
                    keyboard.release(-item)
            else:
                keyboard_layout.write(item)
    else:
        # Release any still-pressed modifier keys
        group[1].text = ''
        for item in sequence:
            if isinstance(item, int) and item >= 0:
                keyboard.release(item)
        pixels[key_to_pixel[key_number]] = apps[app_index].macros[key_number][0]
        pixels.show()
        display.refresh()
