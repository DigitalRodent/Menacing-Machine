from maqueen import Maqueen
from microbit import *
bot = Maqueen()

# When the light sensor detects light above 2 'units'
# it activates both front leds
while True:
    display.read_light_level()
    if display.read_light_level() < 2:
        bot.led_right(1)
        bot.led_left(1)
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,9)

# When the light sensor detects light below 2 'units'
# nothing is activated
    else:
        bot.led_right(0)
        bot.led_left(0)
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,0)
                
