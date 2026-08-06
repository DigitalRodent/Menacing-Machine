
from maqueen import Maqueen
import objectavoidance
from microbit import *
import utime as u

bot = Maqueen()
fast = 255
slow = 50
slowest = 200 # This isn't actually the slowest speed, but I can't be bothered to refactor in thonny.
seecount = 0 # Define counts for various purposes
sweepcount = 0
nocount = 0
lastdir = True # True is Right, False is Left
# Turn commands
while True:
    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed(): # Turn on main loop if microphone detects sound or A is presse
        while True:
            distance_in_cm = bot.ultrasound_measure()
            print(distance_in_cm)
            if distance_in_cm in (0, 0.5):
                while seecount < 10: # If we've seen it less than 10 times, measure again.
                    distance_in_cm = bot.ultrasound_measure()
                    if distance_in_cm in (0, 3):
                        seecount += 1
                    if distance_in_cm > 3:
                        break
                        seecount = 0 # If its more than 3 cm away, ignore and set sightings to 0.
                    if seecount >= 10:
                        objectavoidance.avoid()
                        seecount = 0
                
            # Full white detected aka no line
            if bot.line_left() and bot.line_right():
                while True: # If full white, attempt to reverse and exit the dead end
                    bot.left(0)
                    bot.right(0)
                    if nocount < 2500:
                        print(nocount)
                        if not lastdir:
                            bot.right(slowest, 1)
                            bot.left(0)
                        else:
                            bot.left(slowest, 1)
                            bot.right(0)
                        if bot.line_left() and bot.line_right(): # If still full white, add to no count.
                            nocount += 1
                        else:
                            break
                            nocount = 0
                    else:# Begin line finding code!!
                        while True:
                            if bot.line_left() and bot.line_right():
                                pass
                            else:
                                nocount = 0
                                break
                            for i in range(0, 255):
                                print(i)
                                bot.right(i)
                                bot.left(i//5 + 10)
                                u.sleep(0.06)
                                if i == 255:
                                    break
                                if bot.line_left() and bot.line_right():
                                    pass
                                else:
                                    break
                            for i in range (255, 0, -1):
                                print('begin')
                                print(i)
                                bot.right(i)
                                bot.left(i//5 + 10)
                                u.sleep(0.06)
                                if i == 0:
                                    break
                                if bot.line_left() and bot.line_right():
                                    pass
                                else:
                                    break
                    
                        

                
                
            # White left, line right
            if not bot.line_left() and bot.line_right():
                bot.right(fast)
                bot.left(slow, 1)
                lastdir = 1
            # White right, line left
            if not bot.line_right() and bot.line_left():
                bot.left(fast)
                bot.right(slow, 1)
                lastdir = 0
            # Full line
            if not bot.line_left() and not bot.line_right():
                bot.right(fast)
                bot.left(fast)
            if button_a.was_pressed(): # If A is pressed, stop moving and leave the main loop.
                bot.left(0)
                bot.right(0)
                break









 