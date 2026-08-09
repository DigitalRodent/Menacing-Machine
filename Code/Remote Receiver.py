from maqueen import Maqueen
from microbit import *
from linefollow import Robot
import radio
import speech

# Activates the onboard radio receiver, selects 'channel'
radio.on()
radio.config(group=1)
bot_controller = Robot()
running = False

# Scans for signal broadcast
def check_for_message():
    global running
    message = radio.receive()
# Receives signal '1'
    if message == '1':
        print('Received 1')
        speech.say('Oh Blencowe')
        running = True
# Receives signal '2'
    elif message == '2':
        print('Received 2')
        running = False
        speech.say('See you later space cowboy')
    return message

# Constant running
print('Startup')
while True:
    check_for_message()
    if running:
        bot_controller.RoboGobo(check_for_message) # Run check_for_message in RoboGobo so we can check for poll
    else:
        bot_controller.RoboSlobo()
        u = None 




