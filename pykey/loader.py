import os

class KB_Loader:
    """
    Class representing a keyboard procesing loop..
    """

    def __init__(self, folder, keymapclass):
        self._folder = folder
        self._keymapclass = keymapclass
        self._layers = []

    def load(self):
        files = os.listdir(self._folder)
        files.sort()
        for filename in files:
            print(filename)
            if filename.endswith('.py'):
                try:
                    module = __import__(self._folder + '/' + filename[:-3])
                    self._layers.append(self._keymapclass(module.layer))
                except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                        IndexError, TypeError) as err:
                    print(err)
                    pass
        return self._layers
