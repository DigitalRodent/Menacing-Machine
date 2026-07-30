from maqueen import Maqueen
from microbit import *
import utime as u
import music
bot = Maqueen()
fast = 255
slow = 50
slowest = 200
while True:
    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
        while True:
            distance_in_cm = bot.ultrasound_measure()
            print(distance_in_cm)
            if distance_in_cm == -1:
                print('lol')
            elif distance_in_cm > 1:
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
<<<<<<< HEAD:main.py
                u.sleep(0.75)
=======
                break
distance = 0

def on_forever():
    global distance
    distance = Maqueen.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    basic.show_number(distance)
    if distance < 15 and distance != 0:
        Maqueen.control_motor_stop(Maqueen.MyEnumMotor.ALL_MOTOR)
        basic.pause(1000)
    else:
        Maqueen.control_motor(Maqueen.MyEnumMotor.ALL_MOTOR,
            Maqueen.MyEnumDir.FORWARD,
            20)
basic.forever(on_forever)
>>>>>>> 92e8971f07bdd45fb048c06b0717cc895395a3b0:Code/main.py
