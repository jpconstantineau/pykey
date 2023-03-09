# SPDX-FileCopyrightText: 2023 Pierre Constantineau
#
# SPDX-License-Identifier: MIT
"""
Code for CNCEncoderPad running wit BlueMicro840
"""
import board
from digitalio import DigitalInOut, Direction
import os
import time

import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

from pykey.encoderpad import EncoderPad

################################################################
# the following is needed for BlueMicro840 to turn on external VCC and power up the rotary encoder.
vcc = DigitalInOut(board.P0_12)
vcc.direction = Direction.OUTPUT
vcc.value = True

################################################################

blehid = HIDService()

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="BlueMicro")
advertisement = ProvideServicesAdvertisement(blehid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CNCEncoderPad HID"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)

k = Keyboard(blehid.devices)
kl = KeyboardLayoutUS(k)



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

macropad = EncoderPad()

macropad._leds.led_ON(0)
time.sleep(0.25)
macropad._leds.led_ON(1)
time.sleep(0.25)
macropad._leds.led_ON(2)
time.sleep(0.25)
macropad._leds.led_ON(3)
time.sleep(0.25)
macropad._leds.led_ON(4)
time.sleep(0.25)
macropad._leds.led_ON(5)
time.sleep(0.25)
macropad._leds.led_ON(6)
time.sleep(0.25)
macropad._leds.led_ON(7)
time.sleep(0.25)
macropad._leds.led_ON(8)
time.sleep(0.25)
macropad._leds.reset_leds()

kbdev = Keyboard(blehid.devices)
###kbdev = macropad.keyboard
keyboard_layout = KeyboardLayoutUS(kbdev)

active_keys = []
layer_index = 0
last_position = 0
not_sleeping = True
################################################################
# DONE SETTING UP
################################################################
# End of Setup: Lets play some Music to let the user we are ready
if macropad.speaker is not None:
    macropad.speaker.play_startup_tune()

################################################################
# loop-y-loop
################################################################

while True:
    if not ble.connected:
        if not ble.advertising:
            ble.start_advertising(advertisement)
        macropad.speaker.play_shutdown_tune()
    
    if ble.connected:
        key_event = macropad.keys.events.get()
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
                        if (item >= 0xF0) and (item <= 0xFF) :
                            layer_keys_pressed.append(item - 0xF0)
            layer_index = get_active_layer(layer_keys_pressed, layer_count)
            # print(layer_index)
            # print(layers[layer_index].macros[key_number][1])
            group = layers[layer_index].macros[key_number][2]
            color = layers[layer_index].macros[key_number][0]
            if key_event.pressed:
                #macropad.pixels[key_number] = 0xFFFFFF
                #macropad.pixels.show()
                for item in group:
                    if isinstance(item, int):
                        macropad.keyboard.press(item)
                    else:
                        macropad.keyboard_layout.write(item)
            else:
                #macropad.pixels[key_number] = color
                #macropad.pixels.show()
                for item in group:
                    if isinstance(item, int):
                        if item >= 0:
                            macropad.keyboard.release(item)

        position = macropad.encoder
        if position != last_position:
            diff=position-last_position
            #print(diff)
            if diff>0:
                if diff >1:
                    group = layers[layer_index].encoder[2][2]
                else:
                    group = layers[layer_index].encoder[0][2]

            else:
                if diff < -1:
                    group = layers[layer_index].encoder[3][2]
                else:
                    group = layers[layer_index].encoder[1][2]
            for item in group:
                if isinstance(item, int):
                    macropad.keyboard.send(item)
        last_position = position
        time.sleep(0.002)


    
    
# if we end up here, the program will end with a short tune...
if macropad.speaker is not None:
    macropad.speaker.play_shutdown_tune()
