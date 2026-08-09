from maqueen import Maqueen
bot = Maqueen()
bot.motor_right(255)
bot.motor_left(255)
while True:
    speed = accelerometer.get_z()
    print(speed)

