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
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.clear_screen()
        basic.pause(500)
    elif signal == 2:
        music.play(music.tone_playable(330, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
    else:
        RoboGobo()
basic.forever(on_forever)
