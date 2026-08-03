from microbit import *

LEFT_LIGHT_PIN = pin1
RIGHT_LIGHT_PIN = pin2
HEADLIGHT_PIN = pin8

# Threshold below which we consider it "low light".
# analog_read() returns 0-1023. Lower value = darker (less light hitting sensor).
# Tune this by testing in your room: print the values first and see what
# "dark" looks like for your sensors.
LOW_LIGHT_THRESHOLD = 300

headlights_on = False

def set_headlights(state):
    """Turn Maqueen headlights on/off."""
    global headlights_on
    headlights_on = state
    HEADLIGHT_PIN.write_digital(1 if state else 0)

def read_light_level():
    """Average both light sensors and return a single light value."""
    left = LEFT_LIGHT_PIN.read_analog()
    right = RIGHT_LIGHT_PIN.read_analog()
    return (left + right) // 2

# Start with headlights off
set_headlights(False)

while True:
    light_level = read_light_level()

    if light_level < LOW_LIGHT_THRESHOLD and not headlights_on:
        set_headlights(True)
        display.show(Image.SAD)   # dark face icon = low light detected
        sleep(500)
        display.clear()

    elif light_level >= LOW_LIGHT_THRESHOLD and headlights_on:
        set_headlights(False)
        display.show(Image.HAPPY)  # bright face icon = light restored
        sleep(500)
        display.clear()

    sleep(200)  # small delay to avoid flickering / excessive polling