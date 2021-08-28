---
id: sleep
title: Sleep and Power
sidebar_label: Sleep and Power
---

Current consumption on a BLE keyboard is dependent on how efficient the scanning routine is, how eficient it processes keystrokes, if/how the processor is put on hold, and BLE radio usage.

Current consumption of the BLE radio is much higher than that of the processor. However, as BLE messages are only occurring at a specific frequency and are not continuous, their impact on a time-averaged basis is not as significant than the running average of the processor running constantly. 

Reference:
* [Learning Guide](https://learn.adafruit.com/deep-sleep-with-circuitpython/alarms-and-sleep)
* [Docs](https://circuitpython.readthedocs.io/en/latest/shared-bindings/alarm/index.html)
* [Zephyr vs Arduino Power Consumption on the nRF52840](https://www.youtube.com/watch?v=RGR1rowOaX4&t=795s)
* [Bluefruit.begin() causes high power consumption](https://github.com/adafruit/Adafruit_nRF52_Arduino/issues/600)
* [Sleep in Arduino](https://github.com/jpconstantineau/BlueMicro_BLE/blob/master/firmware/sleep.cpp)
* [nRF52840 datasheet](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf)

## Normal Power Consumption

| Case | ZMK  | BlueMicro_BLE | Code Below |
|----- | -------------| --------------------------------------| --------------|
| Framework |Zephyr | Adafruit_nRF52_Arduino | CircuitPython | 
| connected to BLE | 700-750 uA | 950-1000 uA | 6.8-7.2 mA |
| Sleeping | 50 uA | 60 uA | 160-200uA |
| measured using | PPK | PPK | PPK2

I tested the code below to see if time.sleep and alarm.light_sleep differred in power consumption and if one was better than the other.
Unfortunately, both had the same power consumption with an average of 7mA.
Such a high current is similar to the issue filed on the Adafruit nRF52 arduino package when the cryptocell was implemeented and powr consumption jumped up significantly.

## Deep Sleep vs Sleeping Beauty (System OFF)
The CircuitPython implementation of deep sleep isn't the same as what was implemented for the BlueMicro_BLE firmware.  The arduino implementation is quite simple:
* setup the anode (+ve) side of the keyboard matrix to be outputs and put them `HIGH`. This will apply the necessary voltage to enable a trigger on the cathode side (-ve) when a key is pressed while sleeping 
* setup GPIOs on the cathode side of the matrix to be `INPUT_PULLDOWN_SENSE` 
* call `sd_power_system_off();` This is the softdevice call to completely power down the chip.

At that point the chip powers down but when a key is pressed, it wakes up as if rebooting from a reset or a power up.  The `RESETREAS` register would have the E bit set (see datasheet, page 75) on powerup. The bootloader does not appear to clear-out the `RESETREAS` Regiter but does clear the `GPREGRET` register if appropriate. [See code here](https://github.com/adafruit/Adafruit_nRF52_Bootloader/blob/master/src/main.c#L182)

When referring to the nRF52840 Datasheet, page 149 and 150, we see that this wake-up mechanism is simple (POWER Peripheral uses the DETECT signal to exit from System OFF mode) 

``` python
#pylint: disable = line-too-long
import time
import alarm
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
from adafruit_hid.keycode import Keycode as KC

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

keyboard = Keyboard(hid.devices)
kl = KeyboardLayoutUS(keyboard)
layer = 0
keymap = ((KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H),
        (KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H))

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
            key = keymap[layer][key_event.key_number]
            if key_event.pressed:
                keyboard.press(key)
            else:
                keyboard.release(key)
        # time.sleep(0.02) # 6-7mA
        # nothing 6-7mA
        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 0.02) # 6-7mA too...
        # Do a light sleep until the alarm wakes us.
        alarm.light_sleep_until_alarms(time_alarm)
        # Finished sleeping. Continue from here.
    keys.deinit() # must release the pins in order to setup wake up alarm.
    pin_alarm = alarm.pin.PinAlarm(pin=board.P0_29, value=False, pull=True)
    alarm.exit_and_deep_sleep_until_alarms(pin_alarm)  # 160-200uA
    ble.start_advertising(advertisement)
```