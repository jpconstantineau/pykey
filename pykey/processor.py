import time
import rainbowio

class KB_Processor:
    """
    Class representing a keyboard procesing loop..
    """

    def __init__(self, hardware, keymaps, layout):
        self._hardware = hardware
        self._keyboard = self._hardware.keyboard
        self._keys = self._hardware.keys
        self._keymaps = keymaps
        self._layer_count = len(self._keymaps)
        self._layout = layout(self._keyboard)
        self._pixels = self._hardware.pixels

        if not keymaps:
            print('NO KEYMAP FILES FOUND')
            while True:
                pass

    def rainbow_cycle(self, number):
        if self._pixels is not None:
            for i in range(61):
                rc_index = (i * 256 // 61) +number
                self._pixels[i] = rainbowio.colorwheel(rc_index & 255)
            self._pixels.show()

    def get_active_layer(self, layer_keys_pressed, layer_count):
        tmp = 0
        if len(layer_keys_pressed)>0:
            for layer_id in layer_keys_pressed:
                if layer_id > tmp: # use highest layer number
                    tmp = layer_id
        if tmp >= layer_count:
            tmp = layer_count-1
        return tmp


    def go(self):
        if self._hardware.speaker is not None:
            self._hardware.speaker.play_startup_tune()
        active_keys = []
        not_sleeping = True
        layer_index = 0
        i = 0
        while not_sleeping:
            key_event = self._keys.events.get()
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
                    group = self._keymaps[0].macros[active_key][2]
                    for item in group:
                        if isinstance(item, int):
                            if (item >= 0xF0) and (item <= 0xFF) :
                                layer_keys_pressed.append(item - 0xF0)
                layer_index = self.get_active_layer(layer_keys_pressed, self._layer_count)
                # print(layer_index)
                # print(layers[layer_index].macros[key_number][1])
                group = self._keymaps[layer_index].getkeycodes(key_number)
                #color = self._keymaps[layer_index].macros[key_number][0]
                if key_event.pressed:
                   # update_pixels(color)
                    for item in group:
                        if isinstance(item, int):
                            self._hardware.keyboard.press(item)
                        else:
                            self._hardware.keyboard_layout.write(item)
                else:
                    for item in group:
                        if isinstance(item, int):
                            if item >= 0:
                                self._hardware.keyboard.release(item)
                  #  update_pixels(0x000000)
            else:
                i = i+1
                self.rainbow_cycle(i)
            time.sleep(0.002)

    def test(self):
        if self._hardware.speaker is not None:
            self._hardware.speaker.play_startup_tune()
        active_keys = []
        not_sleeping = True
        layer_index = 0
        i = 0
        while not_sleeping:
            key_event = self._keys.events.get()
            if key_event:
                key_number = key_event.key_number
                # keep track of keys being pressed
                print(key_event)
                print('position:', end=' ')
                print(self._hardware.key_to_position[key_number])
                print('back to key:', end=' ')
                print(self._hardware.position_to_key[self._hardware.key_to_position[key_number]])
                if key_event.pressed:
                    active_keys.append(key_number)
                else:
                    active_keys.remove(key_number)
                if key_event.pressed:
                    self._pixels[self._hardware.key_to_position[key_number]] = 0xFFFFFF
                    self._hardware.speaker.start_tone(440)
                    print
                else:
                    self._pixels[self._hardware.key_to_position[key_number]] = 0x000000
                    self._hardware.speaker.stop_tone()
            else:
                i = i+1
                self.rainbow_cycle(i)
                for active_key in active_keys:
                    self._pixels[self._hardware.key_to_position[active_key]] = 0xFFFFFF
                self._pixels.show()
            time.sleep(0.002)