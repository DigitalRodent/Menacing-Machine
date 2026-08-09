from maqueen import Maqueen
from microbit import *
import radio
bot = Maqueen()
radio.on()
    

signal = 0
radio.config(group=1)
signal = 0

while True:
    if button_a.was_pressed():
        signal = 1
        signal_send()

    if button_b.was_pressed():
        signal = 2
        signal_send()

