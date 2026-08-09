from maqueen import Maqueen
bot = Maqueen()

z_strength = accelerometer.get_z() # Checks accelerometer value
# Lowest value of led
low_bound = 0
# Highest Value of led
high_bound = 9
brightness = max(low_bound, min(z_strength // 100, high_bound)) # Floor divide the accelerometer value by 100 and clamp
# Sets pixels
for y in range(5):
    for x in range(5):
        display.set_pixel(x, y, brightness)