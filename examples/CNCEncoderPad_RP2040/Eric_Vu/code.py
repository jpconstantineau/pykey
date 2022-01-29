"""
Based on the Adafruit Macropad Hotkeys code located
https://learn.adafruit.com/macropad-hotkeys/project-code

Adapted for the CNCEncoderPad_RP2040. Macro setups are stored in the
/macros folder (configurable below), load up just the ones you're likely to
use. Plug into computer's USB port, use dial to select an application macro
set, press MACROPAD keys to send key sequences and other USB protocols.
"""

# pylint: disable=import-error, unused-import, too-few-public-methods

import os
import time
from pykey.encoderpad import EncoderPad


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
        self.encoder = appdata['encoder']

    def switch(self):
        """ Activate application settings; and LED colors. """
        print(self.name)
        for i in range(9):
            if i < len(self.macros): # Key in use, set label + LED color
                macropad.pixels[i] = self.macros[i][0]
            else:  # Key not in use, no label or LED
                macropad.pixels[i] = 0
        macropad.keyboard.release_all()
        macropad.consumer_control.release()
        macropad.mouse.release_all()
        macropad.pixels.show()


# INITIALIZATION -----------------------

macropad = EncoderPad()
macropad.pixels.auto_write = False


# Load all the macro key setups from .py files in MACRO_FOLDER
apps = []
files = os.listdir(MACRO_FOLDER)
files.sort()
for filename in files:
    if filename.endswith('.py'):
        try:
            module = __import__(MACRO_FOLDER + '/' + filename[:-3])
            apps.append(App(module.layer))
        except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                IndexError, TypeError) as err:
            print("ERROR in", filename)
            import traceback
            traceback.print_exception(err, err, err.__traceback__)

if not apps:
    print('NO MACRO FILES FOUND')
    while True:
        pass
print(len(apps))

last_position = 0
layer_switch_mode = False
app_index = 0
apps[app_index].switch()


# MAIN LOOP ----------------------------

while True:
    # Read encoder position and get keys events.
    position = macropad.encoder

    if layer_switch_mode==True:
        if position != last_position:
            print(position)
            app_index = position % len(apps)
            apps[app_index].switch()
            last_position = position
    else:
        if position != last_position:
            diff=position-last_position
            last_position = position
            if diff>0:
                sequence = apps[app_index].encoder[0][2]
            else:
                sequence = apps[app_index].encoder[1][2]
            for item in sequence:
                if isinstance(item, int):
                    macropad.keyboard.send(item)
                elif isinstance(item, float):
                    time.sleep(item)
                elif isinstance(item, str):
                    macropad.keyboard_layout.write(item)
                elif isinstance(item, list):
                    for code in item:
                        if isinstance(code, int):
                            macropad.consumer_control.press(code)
                            macropad.consumer_control.release()
                        if isinstance(code, float):
                            time.sleep(code)
                elif isinstance(item, dict):
                    if 'buttons' in item:
                        if item['buttons'] >= 0:
                            macropad.mouse.press(item['buttons'])
                        else:
                            macropad.mouse.release(-item['buttons'])
                    macropad.mouse.move(item['x'] if 'x' in item else 0,
                                        item['y'] if 'y' in item else 0,
                                        item['wheel'] if 'wheel' in item else 0)



    event = macropad.keys.events.get()
    if not event or event.key_number >= len(apps[app_index].macros):
        continue # No key events, or no corresponding macro, resume loop

    key_number = event.key_number
    pressed = event.pressed

    if key_number == 0:
        if pressed == True:
            layer_switch_mode = True
        else:
            layer_switch_mode = False

    if layer_switch_mode==True:
        print("layer_switch_mode")
        print(position)
        if position != last_position:
            print(position)
            app_index = position % len(apps)
            apps[app_index].switch()
            last_position = position


    if layer_switch_mode==False:

    # If code reaches here, a key or the encoder button WAS pressed/released
    # and there IS a corresponding macro available for it...other situations
    # are avoided by 'continue' statements above which resume the loop.

        sequence = apps[app_index].macros[key_number][2]
        if pressed:
            # 'sequence' is an arbitrary-length list, each item is one of:
            # Positive integer (e.g. Keycode.KEYPAD_MINUS): key pressed
            # Negative integer: (absolute value) key released
            # Float (e.g. 0.25): delay in seconds
            # String (e.g. "Foo"): corresponding keys pressed & released
            # List []: one or more Consumer Control codes (can also do float delay)
            # Dict {}: mouse buttons/motion (might extend in future)
            if key_number < 9:
                macropad.pixels[key_number] = 0xFFFFFF
                macropad.pixels.show()
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        macropad.keyboard.press(item)
                    else:
                        macropad.keyboard.release(-item)
                elif isinstance(item, float):
                    time.sleep(item)
                elif isinstance(item, str):
                    macropad.keyboard_layout.write(item)
                elif isinstance(item, list):
                    for code in item:
                        if isinstance(code, int):
                            macropad.consumer_control.press(code)
                            macropad.consumer_control.release()
                        if isinstance(code, float):
                            time.sleep(code)
                elif isinstance(item, dict):
                    if 'buttons' in item:
                        if item['buttons'] >= 0:
                            macropad.mouse.press(item['buttons'])
                        else:
                            macropad.mouse.release(-item['buttons'])
                    macropad.mouse.move(item['x'] if 'x' in item else 0,
                                        item['y'] if 'y' in item else 0,
                                        item['wheel'] if 'wheel' in item else 0)
        else:
            # Release any still-pressed keys, consumer codes, mouse buttons
            # Keys and mouse buttons are individually released this way (rather
            # than release_all()) because pad supports multi-key rollover, e.g.
            # could have a meta key or right-mouse held down by one macro and
            # press/release keys/buttons with others. Navigate popups, etc.
            for item in sequence:
                if isinstance(item, int):
                    if item >= 0:
                        macropad.keyboard.release(item)
                elif isinstance(item, dict):
                    if 'buttons' in item:
                        if item['buttons'] >= 0:
                            macropad.mouse.release(item['buttons'])
                    elif 'tone' in item:
                        macropad.consumer_control.release()
            if key_number < 9: # No pixel for encoder button
                macropad.pixels[key_number] = apps[app_index].macros[key_number][0]
                macropad.pixels.show()
