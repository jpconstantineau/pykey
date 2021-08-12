import board
import rotaryio
import keypad
import usb_hid
import time
import pwmio
import alarm
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode as KC

""" 
CNCEncoderPad
#define MATRIX_ROW_PINS { 6, 45, 28 }
#define MATRIX_COL_PINS { 9, 13, 38 }
#define ENCODER_PAD_A  26 
#define ENCODER_PAD_B  30 

#define VBAT_PIN  4
#define VCC_PIN 12
#define VCC_POLARITY_ON 1

#define SPEAKER_PIN 29

#define LEDCOL0 8
#define LEDCOL1 2
#define LEDCOL2 3
#define LEDROW0 10
#define LEDROW1 20
#define LEDROW2 24

"""
# define hardware
buzzer = pwmio.PWMOut(board.P0_29, variable_frequency=True)
buzzer.frequency = 440
OFF = 0
ON = 2**15
not_sleeping = True

keys = keypad.KeyMatrix(
    row_pins=(board.P0_06, board.P1_13, board.P0_28),
    column_pins=(board.P0_09, board.P0_13,board.P1_06),
    columns_to_anodes=False,
)

encoder = rotaryio.IncrementalEncoder(board.P0_30, board.P0_26)
last_position = 0

layer = 0
keymap = ((KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H,KC.I),
        (KC.A,KC.B,KC.C,KC.D,KC.E,KC.F,KC.G,KC.H,KC.I))

# setup variables
encoder_map = ((KC.DOWN_ARROW,KC.UP_ARROW),
                (KC.LEFT_ARROW, KC.RIGHT_ARROW))
buzzer.duty_cycle = ON
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.frequency = 880 # 
time.sleep(0.05)
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.duty_cycle = OFF

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard) 


while not_sleeping:
    key_event = keys.events.get()
    if key_event:
        key = keymap[layer][key_event.key_number]
        if key_event.pressed:
            keyboard.press(key)
        else:
            keyboard.release(key)

    position = encoder.position
    if position != last_position:
        diff=position-last_position
        if diff>0:
            keyboard.send(encoder_map[layer][0])
        else:
            keyboard.send(encoder_map[layer][1])
    last_position = position
    time.sleep(0.001)
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)