from maqueen import Maqueen
from microbit import *
import utime
bot = Maqueen()

distance = 0

def on_forever():
    global distance
    distance = Maqueen.read_ultrasonic(DigitalPin.P13, DigitalPin.P14)
    basic.show_number(distance)
    if distance < 15 and distance != 0:
        Maqueen.control_motor_stop(Maqueen.MyEnumMotor.ALL_MOTOR)
        basic.pause(1000)
    else:
        Maqueen.control_motor(Maqueen.MyEnumMotor.ALL_MOTOR,
            Maqueen.MyEnumDir.FORWARD,
            20)
basic.forever(on_forever)