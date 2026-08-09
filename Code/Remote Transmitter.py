from maqueen import Maqueen
from microbit import *
import radio
bot = Maqueen()
radio.on()
    
# Sets the radio channel that the signals will be transmitted on (group = channel)
signal = 0
radio.config(group=1)
signal = 0

# When button 'a' is pressed, a signal is sent on channel '1'
while True:
    if button_a.was_pressed():
        signal = 1
        signal_send()

# When button 'b' is pressed, a signal is sent on channel '1'
    if button_b.was_pressed():
        signal = 2
        signal_send()

