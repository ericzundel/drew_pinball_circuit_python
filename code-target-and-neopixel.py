# code-target-and-neopixel.py
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Shows how to read a switch attached to a target and light a Neopixel Strip"""

import time
import board
# For more information on how to use digitalio on Circuit Python, see
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
from digitalio import DigitalInOut, Direction, Pull
# For more information on how to use the neopixel library on Circuit Python, see
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
import neopixel

# Here are some RGB values for some common colors.
# 0 == LED off and 255 == full brightness
RED    = (255,   0,   0) # 100% red,   0% green, 0% blue
BLACK  = (  0,   0,   0) # 0% of all colors (turns the LED off)

#Initialize the target pins
target1_switch = DigitalInOut(board.GP11)
target1_switch.direction = Direction.INPUT
target1_switch.pull = Pull.UP

#Initialize the neopixel strip
# ** Change this value to connnect the DIN wire on the Neopixel strip to a different pin on the Pico
led_strip1_pin = board.GP16
# ** Change this number to be the number of LEDs on your strips
led_strip1_num_pixels = 10
# This line initialized the library used to control the neopixel strip
led_strip1 = neopixel.NeoPixel(led_strip1_pin, led_strip1_num_pixels, brightness=0.3, auto_write=False)

led_strip1.fill(BLACK)
led_strip1.show()

while True:
    if (target1_switch.value == True):
        # The input has a pull up, so this means the target is not pressed
        led_strip1.fill(BLACK)
        led_strip1.show()
    else:
        # The button is pulled to ground, so the target is pressed
        led_strip1.fill(RED)
        led_strip1.show()
        time.sleep(.25)
