# pylint: disable = line-too-long

from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from pykey.loader import KB_Loader
from pykey.vcolchoc44 import VColChoc44
from pykey.processor import KB_Processor


class Layer:
    """Class representing a layer, for which we have a set
    of macro sequences or keycodes"""

    def __init__(self, layerdata):
        self.name = layerdata["name"]
        self.macros = layerdata["macros"]

    def getcolor(self, keypressed):
        return self.macros[keypressed][0]

    def getdescription(self, keypressed):
        return self.macros[keypressed][1]

    def getkeycodes(self, keypressed):
        return self.macros[keypressed][2]


# Load all the macro key setups from .py files in '/layers'
loader = KB_Loader("/layers", Layer)

processor = KB_Processor(VColChoc44(nkro=False), loader.load(), KeyboardLayoutUS)

processor.go()
