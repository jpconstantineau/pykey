import os
import time
import board
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from keycode import PK_Keycode as KC
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Hardware definition: GPIO where RGB LED is connected. 
pixel_pin = board.P0_15
num_pixels = 1

layer_index = 0

# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'


# CLASSES AND FUNCTIONS ----------------

class Layer:
    """ Class representing a layer, for which we have a set
        of macro sequences or keycodes"""
    def __init__(self, layerdata):
        self.name = layerdata['name']
        self.macros = layerdata['macros']


# INITIALIZATION -----------------------

# Load all the macro key setups from .py files in MACRO_FOLDER
layers = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            layers.append(Layer(module.layer))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            pass

if not layers:
    print('NO MACRO FILES FOUND')
    while True:
        pass



pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


# Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_03, board.P0_28, board.P1_13),
    column_pins=(board.P0_02, board.P0_29, board.P0_30, board.P0_26),
    columns_to_anodes=True,
)


# Neopixel update function
def update_pixels(color):
    for i in range(num_pixels):
        pixels[i] = color
    pixels.show()
        


keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    key_event = keys.events.get()
    if key_event:
        key_number = key_event.key_number
        # print(layers[layer_index].macros[key_number][1])
        group = layers[layer_index].macros[key_number][2]
        if key_event.pressed:
            update_pixels(0x400000) 
            for item in group:
                if isinstance(item, int):
                    keyboard.press(item)
                else:
                    keyboard_layout.write(item)  
        else:
            for item in group:
                if isinstance(item, int):
                    if item >= 0:
                        keyboard.release(item)
            update_pixels(0x004000) 
    time.sleep(0.002)
 