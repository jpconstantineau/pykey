#pylint: disable = line-too-long

from pykey.pykey60 import PyKey60
from pykey.loader import KB_Loader
from pykey.processor import KB_Processor
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

class Layer:
    """ Class representing a layer, for which we have a set
        of macro sequences or keycodes"""
    def __init__(self, layerdata):
        self.name = layerdata['name']
        self.macros = layerdata['macros']
         
    def getcolor(self, keypressed):
        return self.macros[keypressed][0]
     
    def getdescription(self, keypressed):
        return self.macros[keypressed][1]    
   
    def getkeycodes(self, keypressed):
        return self.macros[keypressed][2]
        
# Load all the key setups from .py files in '/layers' using the Layer class defined above
loader = KB_Loader('/layers', Layer)

# Setup the hardware with the layers and layout
processor = KB_Processor(PyKey60(nkro=False), loader.load(), KeyboardLayoutUS)

# Start the Keyboard
processor.go()
