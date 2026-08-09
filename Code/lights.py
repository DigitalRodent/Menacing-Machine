from maqueen import Maqueen
from microbit import *
bot = Maqueen()
while True:
    display.read_light_level()
    if display.read_light_level() < 2:
        bot.led_right(1)
        bot.led_left(1)
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,9)
    else:
        bot.led_right(0)
        bot.led_left(0)
        for y in range(5):
            for x in range(5):
                display.set_pixel(x,y,0)
                
