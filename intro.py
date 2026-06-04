from microbit import *
import music
i2c.init()
i2c.write(0x10, bytearray([0, 0, 15, 1, 15]))
set_volume(150)
while True:
    display.show(Image.SKULL)
    music.play(music.PYTHON)