# code-pinball-prototype
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Example for how to use everything together for the prototype"""

import time
import board
import busio

# For more information on how to use digitalio on Circuit Python, see
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
from digitalio import DigitalInOut, Direction, Pull

# LCD Source code is at https://github.com/dhalbert/CircuitPython_LCD
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# For more information on how to use the neopixel library on Circuit Python, see
# https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel
import neopixel

#################################################################
# Define global variables
# Initialize the score variable
score = 0

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
i2c = busio.I2C(board.GP1, board.GP0)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)

# Create an array to hold the flipper solenoid output objects
flipper_solenoids = [
    DigitalInOut(board.GP2),
]

# Create an array to hold the flipper switch objects
flipper_switches = [
    DigitalInOut(board.GP4),
]

# Create an array to hold the target swtich objects
target_switches = [
    DigitalInOut(board.GP11),
    DigitalInOut(board.GP10),
    DigitalInOut(board.GP9),
    DigitalInOut(board.GP8),
    DigitalInOut(board.GP7)
]

# Here are some RGB values for some common colors.
# 0 == LED off and 255 == full brightness
RED    = (255,   0,   0) # 100% red,   0% green, 0% blue
BLACK  = (  0,   0,   0) # 0% of all colors (turns the LED off)

# End global variables
#################################################################


# setup(): runs one time when the processor starts up
def setup():
    # initialize neopixels

    # initialize targets
    for target_switch in target_switches:
        target1_switch.direction = Direction.INPUT
        target1_switch.pull = Pull.UP

    # initialize flippers solenoids
    for flipper_button in flipper_buttons:
        flipper_button.direction = Direction.INPUT
        flipper_button.pull = Pull.UP

    # Initialize the flipper solenoids relay as an output
    for flipper_solenoid in flipper_solenoids:
        flipper_solenoid.direction = Direction.OUTPUT
        flipper_solenoid.value = False

    # initialize bumper solenoids

    # initialize bumper switches

    # initialize lcd
    lcd.set_backlight(True)

    # Initialize the flipper button as an input


def handle_flippers():
    if (flipper1_button.value == True):
        # The input has a pull up, so this means
        # the value is True when the button is not pressed
        flipper1_solenoid.value = False
    else:
        # The button is pulled to ground, so the switch is pressed
        flipper1_solenoid.value = True


def update_score():
    lcd.clear()
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(0, 1)
    lcd.print("Pinball Wizard")
    # Start at the first line, fifth column (numbering from zero).
    lcd.set_cursor_pos(1, 2)
    lcd.print("Score: ")

    # When printing a number with this library, you need to make sure
    # to convert it to a string, otherwise you'll get an error
    # about a non-iterable being passed to print()
    lcd.print(str(score))

def handle_targets():


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
