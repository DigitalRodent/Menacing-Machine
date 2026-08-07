from Code.main import RoboGobo
from maqueen import Maqueen
from microbit import *

bot = Maqueen()

def on_received_number(receivedNumber):
    global signal
    signal = receivedNumber
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global signal
    signal = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global signal
    signal = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global signal
    signal = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

signal = 0
radio.set_group(1)

def on_forever():
    if signal == 1:
        display.show(Image.HAPPY)

    elif signal == 2:
        display.show(Image.SAD)
    else:
        display.show(Image.SKULL)
basic.forever(on_forever)
