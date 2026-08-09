from maqueen import Maqueen
from microbit import *

bot = Maqueen()

slow = 50
fast = 255
speed = slow  # current speed, starts slow

while True:
    if button_b.was_pressed():
        # Toggle between slow and fast speed
        if speed == slow:
            speed = fast
        else:
            speed = slow
        print(speed)

    bot.motor_left(speed)
    bot.motor_right(speed)