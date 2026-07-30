from maqueen import Maqueen
from microbit import *
import utime
bot = Maqueen()
fast = 255
slow = 50
slowest = 200
while True:
    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
        while True:
            distance_in_cm = robot.ultrasound_measure()
            if distance_in_cm > 10:
                bot.motor_left(50)
                bot.motor_right(50)
            else:
                bot.motor_left(50, 1)
                bot.motor_right(50,1)
                sleep(2)
                bot.motor_left(0)
                bot.motor_right(50)
                sleep(0.5)
                bot.motor_right(0)
