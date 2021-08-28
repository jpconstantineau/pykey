# SPDX-FileCopyrightText: 2021 Pierre Constantineau
# SPDX-License-Identifier: MIT

# This code is currently a work in progress for the prototype hardware
# and is not expected to work as-is on the final hardware
# firmware will be updated.

#pylint: disable = line-too-long
import os
import time
import board
import rotaryio
import keypad
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from pykey.keycode import PK_Keycode as KC
import pykey.lights as lights
from pykey.sounds import Speaker

################################################################
# init board's User Input (keys, buttons, encoders)
# replace with your own pins and stuff
################################################################
# -------------------------------------------
# Hardware definition: Switch Matrix Setup.
# -------------------------------------------
keys = keypad.KeyMatrix(
    row_pins=(board.P0_06, board.P1_13, board.P0_28),
    column_pins=(board.P0_09, board.P0_13,board.P1_06),
    columns_to_anodes=False,
)

# -------------------------------------------
# Hardware definition: Key Switch Setup.
# -------------------------------------------
buttons = None

# -------------------------------------------
# Hardware definition: rotary encoder
# -------------------------------------------
encoder = rotaryio.IncrementalEncoder(board.P0_26, board.P0_30)


################################################################
# init board's LEDs for visual output
# replace with your own pins and stuff
################################################################
# -------------------------------------------
# Hardware definition: GPIO where Neopixel (RGB LED) is connected.
# -------------------------------------------
pixel_pin = None
num_pixels = 0

# -------------------------------------------
# Hardware definition: LED Matrix
# -------------------------------------------
leds = lights.LEDMatrix((board.P0_08,board.P0_02,board.P0_03),(board.P0_24,board.P0_20,board.P0_10),True)
leds.reset_leds()


# -------------------------------------------
# Hardware definition: audio hardware
# -------------------------------------------
speaker = Speaker(board.P0_29)


################################################################
# Peprare to load keymaps...
# No need to replace things
################################################################
# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'


# CLASSES AND FUNCTIONS ----------------
class Layer:
    """ Class representing a layer, for which we have a set
        of macro sequences or keycodes"""
    def __init__(self, layerdata):
        self.name = layerdata['name']
        self.macros = layerdata['macros']
        self.encoder = layerdata['encoder']



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


################################################################
# Initialize common variables
# No need to replace things
################################################################
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
active_keys = []
not_sleeping = True
layer_index = 0
last_position = 0
not_sleeping = True
################################################################
# DONE SETTING UP
################################################################
# End of Setup: Lets play some Music to let the user we are ready
speaker.play_startup_tune()

################################################################
# loop-y-loop
################################################################
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

    position = encoder.position
    if position != last_position:
        diff=position-last_position
        if diff>0:
            group = layers[layer_index].encoder[0][2]

        else:
            group = layers[layer_index].encoder[1][2]
        for item in group:
            if isinstance(item, int):
                keyboard.send(item)
    last_position = position
    time.sleep(0.002)
# if we end up here, the program will end with a short tune...
speaker.play_shutdown_tune()
