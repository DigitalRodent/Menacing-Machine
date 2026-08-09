from maqueen import Maqueen
from microbit import *
from linefollow import Robot
import radio

radio.on()
radio.config(group=1)
bot_controller = Robot()
running = False

def check_for_message():
    global running
    message = radio.receive()
    if message == '1':
        print('Received 1')
        running = True
    elif message == '2':
        print('Received 2')
        running = False    
    return message

print('Startup')
while True:
    check_for_message()
    if running:
        bot_controller.RoboGobo(check_for_message)
    else:
        u = None 



