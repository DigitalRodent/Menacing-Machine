from maqueen import Maqueen
import objectavoidance
from microbit import *
import utime as u
import radio
import speech
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
                print('POLLING')
                print('POLLING')
                print('POLLING')
                print('POLLING')
                # Headlights
                display.read_light_level()
                print('light')
                if display.read_light_level() < 2:
                    bot.led_right(1)
                    bot.led_left(1)
                    
                else:
                    bot.led_right(0)
                    bot.led_left(0)
                # Speedo
                z_strength = accelerometer.get_z()
                display.scroll(z_strength)      # What better way to measure speed than the accelerometer?                 
                # Radio receiver
                if check_messages:
                    return check_messages()
                    return None
                    print('messages')
                
                    
                            
            
            print('INITIATE')
            distance_in_cm = bot.ultrasound_measure()
            print(distance_in_cm)
            
            if distance_in_cm in (0, 3): # If something is within (x, y) cm...
                objectavoidance.avoid() # Avoid it
                seecount = 0
                
            # Full white detected aka no line
            if bot.line_left() and bot.line_right():
                while True: # If full white, attempt to reverse and exit the dead end
                    poll()
                    bot.motor_left(0)
                    bot.motor_right(0)
                    if nocount < 2500: # If we've been lost for less than 2500 ticks
                        print(nocount)
                        if not lastdir: #Attempt to find the line by reversing towards the last direction we were heading
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
                                # Spiral Spiral Spiral
                                # Last ditch effort to find the line
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
    def RoboSlobo(self): # If B is pressed, stop moving and leave the main loop.
                bot.motor_left(0)
                bot.motor_right(0)
                bot.led_right(0)
                bot.led_left(0)
                for y in range(5):
                    for x in range(5):
                         display.set_pixel(x,y,0)







 
