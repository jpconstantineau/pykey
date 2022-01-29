import board
import digitalio
import supervisor
# KMK Settings
supervisor.set_next_stack_limit(4096 + 4096)

# Checks if trigger key is pressed and enables USB Devices if it is
row = digitalio.DigitalInOut(board.ROW1)
col = digitalio.DigitalInOut(board.COL1)
col.switch_to_output(value=1)
row.switch_to_input(pull=digitalio.Pull.DOWN)

if row.value:
    print("trigger key pressed! Keeping ON USB devices")
else:
    print("trigger key not pressed. Turning OFF USB devices")
    import storage
    import usb_cdc
    import usb_midi
    storage.disable_usb_drive()  # disable CIRCUITPY
    usb_cdc.disable()            # disable REPL
    usb_midi.disable()           # disable MIDI

row.deinit()
col.deinit()# Write your code here :-)
