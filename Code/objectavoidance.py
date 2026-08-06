from maqueen import Maqueen
from microbit import *
bot = Maqueen()
import utime as u
import music
def avoid():
    distance_in_cm = bot.ultrasound_measure()
    print(distance_in_cm)
    bot.left(0)
    bot.right(50)
    u.sleep(0.85)
    bot.left(50)
    u.sleep(0.5)
    bot.right(0)
    u.sleep(0.85)
    bot.left(0)