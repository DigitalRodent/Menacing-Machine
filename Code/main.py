
from maqueen import Maqueen
import objectavoidance
from microbit import *
import utime as u

bot = Maqueen()
fast = 255
slow = 50
slowest = 200
lastdir = True # True is Right, False is Left
# Turn commands
while True:
    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
        while True:
            distance_in_cm = bot.ultrasound_measure()
            print(distance_in_cm)
            if distance_in_cm in (-1, -2):
                print('NULL DISTANCE!!!')
            if distance_in_cm in (0, 4):
                print('OBSTACLE!!!!')
                objectavoidance.avoid()
                
            # Full white
            if bot.line_left() and bot.line_right():
                poopy = 1
                bot.left(0)
                bot.right(0)
                if not lastdir:
                    bot.right(slowest, 1)
                    bot.left(0)
                else:
                    bot.left(slowest, 1)
                    bot.right(0)
                
            # White left
            if not bot.line_left() and bot.line_right():
                bot.right(fast)
                bot.left(slow, 1)
                lastdir = 1
            # White right
            if not bot.line_right() and bot.line_left():
                bot.left(fast)
                bot.right(slow, 1)
                lastdir = 0
            # Full black
            if not bot.line_left() and not bot.line_right():
                bot.right(fast)
                bot.left(fast)
            if button_a.was_pressed():
                bot.left(0)
                bot.right(0)
                break



