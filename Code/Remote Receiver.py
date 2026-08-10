from maqueen import Maqueen
from microbit import *
from linefollow import Robot
import radio
import speech

radio.on()
radio.config(group=1)
bot_controller = Robot()
running = False

def check_for_message():
    global running
    message = radio.receive()
    if message == '1':
        print('Received 1')
        speech.say('Oh Blencowe')
        running = True
        if running:
            bot_controller.ChangeSpeed()
    elif message == '2':
        print('Received 2')
        running = False
        speech.say('See you later space cowboy')
    return message

print('Startup')
while True:
    check_for_message()
    if running:
        bot_controller.RoboGobo(check_for_message)
    else:
        bot_controller.RoboSlobo()
        u = None
        




