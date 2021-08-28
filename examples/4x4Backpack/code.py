import os
import time
import board
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from keycode import PK_Keycode as KC
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
    # print(filename)
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

layer_count = len(layers)
# print(layer_count)
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


# Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_03, board.P0_28, board.P1_13),
    column_pins=(board.P0_02, board.P0_29, board.P0_30, board.P0_26),
    columns_to_anodes=True,
)


# Neopixel update function
def update_pixels(thiscolor):
    for i in range(num_pixels):
        pixels[i] = thiscolor
    pixels.show()

def get_active_layer(layer_keys, layer_count):
    tmp = 0
    if len(layer_keys)>0:
        for layer_id in layer_keys:
            if layer_id > tmp: # use highest layer number
                tmp = layer_id
    if tmp >= layer_count:
        tmp = layer_count-1
    return tmp

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
active_keys = []
while True:
    key_event = keys.events.get()
    if key_event:
        key_number = key_event.key_number

        # keep track of keys being pressed for layer determination
        if key_event.pressed:
            active_keys.append(key_number)
        else:
            active_keys.remove(key_number)

        # reset the layers and identify which layer key is pressed.
        layer_keys_pressed = []
        for active_key in active_keys:
            group = layers[0].macros[active_key][2]
            for item in group:
                if isinstance(item, int):
                    if (item >= KC.LAYER_0) and (item <= KC.LAYER_F) :
                        layer_keys_pressed.append(item - KC.LAYER_0)
        layer_index = get_active_layer(layer_keys_pressed, layer_count)
        # print(layer_index)
        # print(layers[layer_index].macros[key_number][1])
        group = layers[layer_index].macros[key_number][2]
        color = layers[layer_index].macros[key_number][0]
        if key_event.pressed:
            update_pixels(color)
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
            update_pixels(0x000000)
    time.sleep(0.002)
