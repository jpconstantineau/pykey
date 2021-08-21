#pylint: disable = line-too-long
import os
import time
import board
import neopixel
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from pykey.keycode import PK_Keycode as KC
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Hardware definition: GPIO where RGB LED is connected.
pixel_pin = board.P1_15
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)


# Hardware definition: Switch Matrix Setup.
keys = keypad.KeyMatrix(
    row_pins=(board.P1_11, board.P0_30, board.P0_02, board.P0_29, board.P0_26),
    column_pins=(
        board.P0_06, board.P0_05, board.P0_08, board.P1_09, board.P0_04,
        board.P0_12, board.P1_06, board.P0_24, board.P0_22, board.P0_13, 
        board.P0_15, board.P0_17, board.P0_20, board.P0_09, board.P0_10,
    ),
    columns_to_anodes=True,
)


# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'


# CLASSES AND FUNCTIONS ----------------

class Layer:
    """ Class representing a layer, for which we have a set
        of macro sequences or keycodes"""
    def __init__(self, layerdata):
        self.name = layerdata['name']
        self.macros = layerdata['macros']


# Neopixel update function
def update_pixels(color):
    for i in range(num_pixels):
        pixels[i] = color
    pixels.show()


# INITIALIZATION -----------------------

# Load all the macro key setups from .py files in MACRO_FOLDER
layers = []

files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    print(filename)
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            layers.append(Layer(module.layer))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print(err)
            pass

if not layers:
    print('NO MACRO FILES FOUND')
    while True:
        pass

layer_count = len(layers)
# print(layer_count)

def get_active_layer(layer_keys_pressed, layer_count):
    tmp = 0
    if len(layer_keys_pressed)>0:
        for layer_id in layer_keys_pressed:
            if layer_id > tmp: # use highest layer number
                tmp = layer_id
    if tmp >= layer_count:
        tmp = layer_count-1
    return tmp


# setup variables
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
active_keys = []
not_sleeping = True
layer_index = 0

while not_sleeping:
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
