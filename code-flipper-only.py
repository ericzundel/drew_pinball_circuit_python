# code-flipper-only
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Example for how to use a button to control a flipper"""

import time
import board
# For more information on how to use digitalio on Circuit Python, see
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
from digitalio import DigitalInOut, Direction, Pull

# Initialize the flipper solenoid relay as an output
flipper1_solenoid = DigitalInOut(board.GP2)
flipper1_solenoid.direction = Direction.OUTPUT
flipper1_solenoid.value = False

# Initialize the flipper button as an input
flipper1_button = DigitalInOut(board.GP4)
flipper1_button.direction = Direction.INPUT
flipper1_button.pull = Pull.UP

while True:
    if (flipper1_button.value == True):
        # The input has a pull up, so this means
        # the value is True when the button is not pressed
        flipper1_solenoid.value = False
    else:
        # The button is pulled to ground, so the switch is pressed
        flipper1_solenoid.value = True

