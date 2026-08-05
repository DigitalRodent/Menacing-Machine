from maqueen import Maqueen
from microbit import *
bot = Maqueen()
import utime as u
import music
def avoid():
    distance_in_cm = bot.ultrasound_measure()
    print(distance_in_cm)