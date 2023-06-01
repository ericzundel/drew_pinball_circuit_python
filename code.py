# This program selects one of the code files
# Uncomment one of the lines below that sets MODE to control
# which one to call
#MODE="flipper-only"
#MODE="lcd-i2c"
#MODE="target-and-neopixel"
MODE="pinball-prototype"

with open("code-"+MODE+".py") as f:
    exec(f.read())
