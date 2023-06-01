# code-lcd-i2c
# Author: Eric Z. Ayers <ericzundel@gmail.com>
"""Simple test for 16x2 character lcd with an I2C LCD backpack."""
import time
import board
import busio

# LCD Source code is at https://github.com/dhalbert/CircuitPython_LCD
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# Initialize the score variable
score = 0

# Initialize I2C bus.
# The Raspberry Pi pico has a number of pin pairs that can be used for I2C.
# One pin is SCL (clock) and the other is SDA (data).  See
# a pin diagram at https://datasheets.raspberrypi.com/pico/Pico-R3-A4-Pinout.pdf
i2c = busio.I2C(board.GP1, board.GP0)

# Talk to the LCD at I2C address 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=20)
lcd.set_backlight(True)

while True:
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
    time.sleep(5)

    lcd.clear()
    lcd.print("Update!")

    # Make the screen scroll sideways
    for i in range (0,20):
        lcd.shift_display(1)
        time.sleep(.25)

    # Bump the score for the next iteration of the loop
    score = score + 100
