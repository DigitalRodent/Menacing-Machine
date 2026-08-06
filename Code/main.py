from maqueen import Maqueen
from microbit import *
import utime as u
import music
bot = Maqueen()
fast = 255
slow = 50
slowest = 200
def RoboGobo():
    while True:
        if on_button_pressed_ab():
            while True:
                distance_in_cm = bot.ultrasound_measure()
                print(distance_in_cm)
                if distance_in_cm == -1:
                    print('lol')
                elif distance_in_cm > 2:
                    bot.motor_right(255)
                    bot.motor_left(255)
                    print('WHOA')
                    music.stop()
                else:
                    going = 1
                    while going:
                        distance_in_cm = bot.ultrasound_measure()
                        print(distance_in_cm)
                        bot.motor_right(50,1)
                        bot.motor_left(50,1)
                        u.sleep(0.3)
                        bot.motor_right(0)
                        bot.motor_left(50)
                        u.sleep(0.45)
                        bot.motor_right(50)
                        u.sleep(0.1)
                        bot.motor_left(0)
                        u.sleep(0.75)
                        bot.motor_left(50)

                        u.sleep(0.1)
                        bot.motor_left(0)
                        u.sleep(0.6)
                        if distance_in_cm == -1:
                            print('hi')
                            break
                        if distance_in_cm > 4:
                            print('hi')
                            break

                    bot.motor_left(50)
                    u.sleep(0.3)
                    bot.motor_right(0)
                    u.sleep(0.75)