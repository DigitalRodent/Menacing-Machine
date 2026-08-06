
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
#             distance_in_cm = bot.ultrasound_measure()
#             print(distance_in_cm)
#             if distance_in_cm in (0, 0.5):
#                 while seecount < 10: # If we've seen it less than 10 times, measure again.
#                     distance_in_cm = bot.ultrasound_measure()
#                     if distance_in_cm in (0, 3):
#                         seecount += 1
#                     if distance_in_cm > 3:
#                         break
#                         seecount = 0 # If its more than 3 cm away, ignore and set sightings to 0.
#                 if seecount >= 10:
#                     with open("output.txt", "w", encoding="utf-8") as file:
#                     file.write(f"Avoided object at {distance_in_cm} after {seecount} sightings")
#                     objectavoidance.avoid()
#                     seecount = 0
                
            # Full white detected aka no line
            if bot.line_left() and bot.line_right():
                while True: # If full white, attempt to reverse and exit the dead end
                    bot.left(0)
                    bot.right(0)
                    if nocount < 5:
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
                        bot.right(fast)
                        bot.left(slow, 1)
                        u.sleep(0.425)
                        if bot.line_left() and bot.line_right():
                            print('Still going') # If we haven't found the line, begin the next sweep
                        else:
                            break
                            nocount = 0
                            sweepcount = 0 # If we have, reset all variables and go back to standard programming
                        bot.left(fast)
                        bot.right(slow, 1)
                        u.sleep(0.425)
                        # SWEEEEEPPPP!
                        if bot.line_left() and bot.line_right():
                            print('Still going')
                        else:
                            break
                            nocount = 0
                            sweepcount = 0
                        sweepcount += 1
                        if sweepcount == 6: # If we've sweeped six times:
                            start_time = u.ticks_ms() # Begin stopwatch
                            while True:
                                bot.left(50)
                                bot.right(0) # Spin right
                                end_time = u.ticks_ms()
                                end_time - start_time = TimeSinceSpin# Record time since stopwatch started
                                print(f'{TimeSinceSpin} Spin Measure')
                                straight_start = u.ticks_ms() # Start stopwatch 2 for the straight
                                if TimeSinceSpin > 3500 : # If the stopwatch reads 3500 miliseconds or more
                                    bot.left(50) # Go forward
                                    bot.right(50)
                                    if bot.line_left() and bot.line_right(): # If we dont have a line
                                        print('Still forward') # Keep going forward
                                    else: # If we do
                                            break # Standard programming
                                    straight_end = u.ticks_ms()
                                    straight_end - straight_start = TimeSinceStraight

                                    print(f'{TimeSinceStraight} Straight Measure')
                                    if TimeSinceStraight > 1500:# If we've been going straight for 1500 miliseconds, start sweeping code again
                                        print('Haha')
                                        sweepcount = 0
                                    else:
                                        print('Go Still My Boy')
                                if bot.line_left() and bot.line_right():
                                    print('Spinning still')
                                else:
                                    sweepcount = 0
                                    nocount = 0
                                    break
                            sweepcount = 0
                            
                    
                        

                
                
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






