#pylint: disable = line-too-long
import os

from pykey.pykey60 import PyKey60
from pykey.processor import PK_Processor

# CONFIGURABLES ------------------------

MACRO_FOLDER = '/layers'

# CLASSES AND FUNCTIONS ----------------

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


processor = KB_Processor(PyKey60(nkro=False), layers)

processor.go()
