---
id: sound
title: Sound and Buzzers
sidebar_label: Sounds
---

If you have a buzzer connected to a GPIO, you can play tunes on it.

Try the example below by changing the pin definition

``` python
import board
import time
import pwmio


# define audio hardware
buzzer = pwmio.PWMOut(board.P1_13, variable_frequency=True)
OFF = 0
ON = 2**15
not_sleeping = True


# End of Setup Music
buzzer.duty_cycle = ON
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.frequency = 880 # 
time.sleep(0.05)
buzzer.frequency = 440 # 
time.sleep(0.05)
buzzer.duty_cycle = OFF
```



