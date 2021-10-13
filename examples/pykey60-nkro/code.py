#pylint: disable = line-too-long
import os
import time
import rainbowio
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from pykey.pykey60 import PyKey60  #Note:  In order for this import to work you will need the file pykey/pykey60.py in a folder called pykey on your board

hardwaredef = PyKey60(nkro=False)

pixels = hardwaredef.pixels

cyclecount = 0

def rainbow_cycle(wait):
        num_pixels = 61
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + wait
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()


buzzer = hardwaredef.speaker
OFF = 0
ON = 2**15

# Hardware definition: Switch Matrix Setup.
keys = hardwaredef.keys

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
    num_pixels = 61
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
keyboard = hardwaredef.keyboard
keyboard_layout = KeyboardLayoutUS(keyboard)
active_keys = []
not_sleeping = True
layer_index = 0

if hardwaredef.speaker is not None:
    hardwaredef.speaker.play_startup_tune()

while not_sleeping:
    key_event = keys.events.get()

    if key_event:
        key_number = key_event.key_number
        cyclecount = cyclecount +1
        rainbow_cycle(cyclecount)

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
                    if (item >= 0xF0) and (item <= 0xFF) :
                        layer_keys_pressed.append(item - 0xF0)
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
    time.sleep(0.002)
