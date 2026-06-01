
from maqueen import Maqueen
from microbit import *
import utime
bot = Maqueen()
fast = 200
slow = 100
slowest = 100
lastdir = True
while True:
    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
        while True:
            # Full white
            if bot.line_left() and bot.line_right():
                bot.motor_left(0)
                bot.motor_right(0)
                if not lastdir:
                    bot.motor_right(slowest, 1)
                    bot.motor_left(0)
                else:
                    bot.motor_left(slowest, 1)
                    bot.motor_right(0)
            # Black left
            if not bot.line_left() and bot.line_right():
                bot.motor_right(fast)
                bot.motor_left(slow, 1)
                display.show(Image.SKULL)
                lastdir = 1
            # Black right
            if not bot.line_right() and bot.line_left():
                bot.motor_left(fast)
                bot.motor_right(slow, 1)
                display.show(Image.HAPPY)
                lastdir = 0
            # Full black
            if not bot.line_left() and not bot.line_right():
                bot.motor_right(fast)
                bot.motor_left(fast)
                display.show(Image.SAD)
            if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
                bot.motor_left(0)
                bot.motor_right(0)
                break
