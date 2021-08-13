---
id: neopixels
title: NeoPixels: RGB LEDs
sidebar_label: RGB LEDs
---

For basic information on NeoPixels and RGB LEDs, refer to this great tutorial from [Adafruit](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel)


``` python
import time
import board
import neopixel
import rainbowio

pixel_pin = board.P0_15
num_pixels = 8

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow_cycle(0.05) 

```