from maqueen import Maqueen
from microbit import *
bot = Maqueen()
while True:
    display.scroll(display.read_light_level())