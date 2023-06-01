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

# Status LED that blinks so you can tell the code is running
status_led = DigitalInOut(board.GP15)

# Create an array to hold array of Neopixel strip objects
led_strips = [
    neopixel.NeoPixel(board.GP16, 10, brightness=0.3, auto_write=False),
    neopixel.NeoPixel(board.GP17, 10, brightness=0.3, auto_write=False),
    neopixel.NeoPixel(board.GP18, 10, brightness=0.3, auto_write=False),
    neopixel.NeoPixel(board.GP19, 10, brightness=0.3, auto_write=False),
    neopixel.NeoPixel(board.GP20, 10, brightness=0.3, auto_write=False),
    neopixel.NeoPixel(board.GP21, 10, brightness=0.3, auto_write=False)
]

# Create an array to hold the flipper solenoid output objects
flipper_solenoids = [
    DigitalInOut(board.GP2),
    DigitalInOut(board.GP3)
]

# Create an array to hold the flipper button objects
flipper_buttons = [
    DigitalInOut(board.GP4),
    DigitalInOut(board.GP5)
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
    print("setup()")

    # initialize status LED
    status_led.direction = Direction.OUTPUT
    status_led.direction = Direction.OUTPUT
    status_led.value = True

    # initialize neopixels
    # Turn off all the LED strips
    for led_strip in led_strips:
        led_strip.fill(BLACK)
        led_strip.show()

    # initialize targets
    for target_switch in target_switches:
        target_switch.direction = Direction.INPUT
        target_switch.pull = Pull.UP

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
    update_score()

def handle_flippers():
    for flipper_num in range(0, len(flipper_buttons)):
        if (flipper_buttons[flipper_num].value == True):
            # The input has a pull up, so this means
            # the value is True when the button is not pressed
            flipper_solenoids[flipper_num].value = False
        else:
            print("Flipper " + str(flipper_num) + " is activated.")
            # The button is pulled to ground, so the switch is pressed
            flipper_solenoids[flipper_num].value = True


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
    for target_num in range(0,len(target_switches)):
        if (target_switches[target_num].value == True):
            # The input has a pull up, so this means the target is not pressed
            led_strips[target_num].fill(BLACK)
            led_strips[target_num].show()
        else:
            # The button is pulled to ground, so the target is pressed
            led_strips[target_num].fill(RED)
            led_strips[target_num].show()
            score = score + 100

def handle_bumpers():
    pass

def update_status_led():
    fractional_secs = time.monotonic() % 1

    # Blink on 2x per second
    if ((fractional_secs > 0 and fractional_secs < .25)
    or (fractional_secs > .5 and fractional_secs < .75)):
        status_led.value = True
    else:
        status_led.value = False

def main_loop():
    old_score = score

    update_status_led()
    handle_flippers()
    handle_targets()
    handle_bumpers()

    if (score != old_score):
        update_score()

#####################################################################
# No need to edit below here. This code just enforces that setup()
# runs once and main_loop() is called repeatedly.


setup()

while True:
    main_loop()
