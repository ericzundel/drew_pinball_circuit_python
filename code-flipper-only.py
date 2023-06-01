# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials NeoPixel example"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# Initialize the flipper solenoid and switch (button)
flipper1_solenoid = DigitalInOut(board.GP2)
flipper1_solenoid.direction = Direction.OUTPUT
flipper1_solenoid.value = False

flipper1_button = DigitalInOut(board.GP4)
flipper1_button.direction = Direction.INPUT
flipper1_button.pull = Pull.UP

while True:
    if (flipper1_button.value == True):
        # The input has a pull up, so this means the switch is not pressed
        flipper1_solenoid.value = False
    else:
        # The button is pulled to ground, so the switch is pressed
        flipper1_solenoid.value = True

