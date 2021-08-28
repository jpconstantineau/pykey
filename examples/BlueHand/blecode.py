#pylint: disable = line-too-long
import time
import board
import keypad
import pwmio
import adafruit_ble
from adafruit_ble.advertising import Advertisement
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.standard.hid import HIDService
from adafruit_ble.services.standard.device_info import DeviceInfoService
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# define audio hardware
buzzer = pwmio.PWMOut(board.P1_13, variable_frequency=True)
OFF = 0
ON = 2**15
not_sleeping = True

# define key GPIOs
keys = keypad.Keys(pins=(board.P0_29,board.P0_02,board.P0_28,board.P0_03,board.P0_10,board.P0_09,board.P0_24,board.P0_13),value_when_pressed=False)


hid = HIDService()

device_info = DeviceInfoService(software_revision=adafruit_ble.__version__,
                                manufacturer="Adafruit Industries")
advertisement = ProvideServicesAdvertisement(hid)
advertisement.appearance = 961
scan_response = Advertisement()
scan_response.complete_name = "CircuitPython HID"

ble = adafruit_ble.BLERadio()
if not ble.connected:
    print("advertising")
    ble.start_advertising(advertisement, scan_response)
else:
    print("already connected")
    print(ble.connections)

k = Keyboard(hid.devices)
kl = KeyboardLayoutUS(k)





# End of Setup Music
buzzer.duty_cycle = ON
buzzer.frequency = 440
time.sleep(0.05)
buzzer.frequency = 880
time.sleep(0.05)
buzzer.frequency = 440
time.sleep(0.05)
buzzer.duty_cycle = OFF

while True:
    while not ble.connected:
        pass
    print("Start typing:")
    while ble.connected:
        key_event = keys.events.get()
        if key_event:
            print(key_event)
    ble.start_advertising(advertisement)
