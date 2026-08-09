from maqueen import Maqueen
from microbit import *
bot = Maqueen()
import utime as u
import music
import speech
# When it detects an object it does robot kung-fu
def avoid():
    speech.say('Get out of the way my clanker')
    distance_in_cm = bot.ultrasound_measure()
    print(distance_in_cm)
    bot.motor_left(50,1)
    bot.motor_right(50,1)
    print('1')
    u.sleep(0.5)
    speaker.on()
    music.pitch(800)
    bot.motor_left(0)
    bot.motor_right(50)
    print('2')
    u.sleep(1)
    bot.motor_left(50)
    print('3')
    u.sleep(1)
    bot.motor_right(0)
    print('4')
    u.sleep(0.85)
    bot.motor_right(50)
    music.stop()
