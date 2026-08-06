from maqueen import Maqueen
from microbit import *

bot = Maqueen()

def on_button_pressed_a():
    global signal
    signal = 1
input.on_button_pressed(button_a, on_button_pressed_a)

def on_button_pressed_ab():
    global signal
    signal = 0
input.on_button_pressed(button_ab, on_button_pressed_ab)

def on_button_pressed_b():
    global signal
    signal = 2
input.on_button_pressed(button_b, on_button_pressed_b)

signal = 0
radio.set_group(1)
signal = 0

def on_forever():
    radio.send_number(signal)
basic.forever(on_forever)

while True:
    if button_a.is_pressed():
        display.show(Image.HAPPY)
    if button_b.is_pressed():
        display.show(Image.SAD)