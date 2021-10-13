# Note: If certain keys are not fully supported by the example KB_Keycode module, you may be able to work around this:

* If you absolutely must have an unsupported character then you may replace the Key Sequence for that key with something that follows the pattern of:
 [ "Example Character" ] be aware that this key will only do this character or sequence of characters...it will not change when you hold down'Shift' or 'Control'

* If you need the key to type a sentence then you may replace the Key Sequence for that key with something that follows the pattern of:
 ["Example sentence"]

* If you need the key to enter two different keys at the same time then you may replace the Key Sequence for that Key with something that follows the pattern of:
 [ KC.LEFT_CONTROL, KC.C ] (this would make it a copy button)  Please note that in this example the order of the key presses may matter.

* If you find yourself trying to enter a complex series of key presses and find that the keyboard continues to press KC.LEFT_CONTROL, for instance, you may want to
 replace the Key Sequence for that Key with something that follows the pattern of:
 [ KC.LEFT_CONTROL, -KC.LEFT_CONTROL ]  (note the placement of the '-' to designate that you wish to stop pressing that key)

* To see the full list of supported KB_Kecode characters type in the CircuitPython REPL:
- from pykey.keycode import KB_Keycode
- print(dir(KB_Keycode))
