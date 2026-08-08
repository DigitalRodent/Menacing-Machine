
from maqueen import Maqueen
import objectavoidance
from microbit import *
import utime as u
import radio
bot = Maqueen()

class Robot:
    def RoboGobo(self, check_messages=None):
            radio.on()
            message = radio.receive()
            fast = 255
            slow = 50
            slowest = 200 # This isn't actually the slowest speed, but I can't be bothered to refactor in thonny.
            seecount = 0 # Define counts for various purposes
            sweepcount = 0
            nocount = 0
            lastdir = True # True is Right, False is Left
            
            def poll():
                if check_messages:
                    return check_messages()
                return None
            
            print('INITIATE')
            distance_in_cm = bot.ultrasound_measure()
            print(distance_in_cm)
            
            if distance_in_cm in (0, 0.5): # If something is within half a cm...
                while seecount < 10: # If we've seen it less than 10 times, measure again.
                    poll()
                    distance_in_cm = bot.ultrasound_measure()
                    if distance_in_cm in (0, 3):
                        seecount += 1
                    if distance_in_cm > 3:
                        break
                        seecount = 0 # If its more than 3 cm away, ignore and set sightings to 0.
                    if seecount >= 10:
                        objectavoidance.avoid() # Avoid it
                        seecount = 0
                
            # Full white detected aka no line
            if bot.line_left() and bot.line_right():
                while True: # If full white, attempt to reverse and exit the dead end
                    poll()
                    bot.motor_left(0)
                    bot.motor_right(0)
                    if nocount < 2500:
                        print(nocount)
                        if not lastdir:
                            bot.motor_right(slowest, 1)
                            bot.motor_left(0)
                        else:
                            bot.motor_left(slowest, 1)
                            bot.motor_right(0)
                        if bot.line_left() and bot.line_right(): # If still full white, add to no count.
                            nocount += 1
                        else:
                            break
                            nocount = 0
                    else:# Begin line finding code if we still havent found it!!
                        while True:
                            poll()
                            if bot.line_left() and bot.line_right():
                                pass
                            else:
                                nocount = 0
                                break
                            for i in range(0, 255):
                                poll()
                                print(i)
                                bot.motor_right(i)
                                bot.motor_left(i//5 + 10)
                                u.sleep(0.06)
                                if i == 255:
                                    break
                                if bot.line_left() and bot.line_right():
                                    pass
                                else:
                                    break
                            for i in range (255, 0, -1):
                                poll()
                                print('begin')
                                print(i)
                                bot.motor_right(i)
                                bot.motor_left(i//5 + 10)
                                u.sleep(0.06)
                                if i == 0:
                                    break
                                if bot.line_left() and bot.line_right():
                                    pass
                                else:
                                    break
                    
                        

                
                
            
            poll()
            # White left, line right
            if not bot.line_left() and bot.line_right():
                bot.motor_right(fast)
                bot.motor_left(slow, 1)
                lastdir = 1
            # White right, line left
            if not bot.line_right() and bot.line_left():
                bot.motor_left(fast)
                bot.motor_right(slow, 1)
                lastdir = 0
            # Full line
            if not bot.line_left() and not bot.line_right():
                bot.motor_right(fast)
                bot.motor_left(fast)
            if button_a.was_pressed(): # If A is pressed, stop moving and leave the main loop.
                bot.motor_left(0)
                bot.motor_right(0)







 
