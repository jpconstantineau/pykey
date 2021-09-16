import time
import board
import neopixel
import rainbowio

# Hardware definition: GPIO where RGB LED is connected. 
pixel_pin = board.A3
num_pixels = 65

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = rainbowio.colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)

while True:
    rainbow_cycle(0.01) 