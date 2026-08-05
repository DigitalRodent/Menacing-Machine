from maqueen import Maqueen
from microbit import *
bot = Maqueen()
import utime as u
import music
def avoid():
    distance_in_cm = bot.ultrasound_measure()
    print(distance_in_cm)
    #music.pitch(500)
    bot.right(50,1)
    bot.left(50,1)
    u.sleep(0.3)
    bot.right(0)
    bot.left(50)
    u.sleep(0.85)
    bot.right(50)
    u.sleep(0.15)
    bot.left(0)
    u.sleep(0.85)
    bot.left(50)
    u.sleep(0.25)
    bot.left(0)
    u.sleep(0.6)
    print('yoy')
    if distance_in_cm == -1:
        print('hey')
    if distance_in_cm > 0:
        print('hi')
        bot.left(50)
        u.sleep(0.3)
        bot.right(0)
        u.sleep(0.75)
fast = 255
slow = 50
slowest = 200
#while True:
#    if microphone.current_event() == SoundEvent.LOUD or button_a.was_pressed():
 #       while True:
  #          distance_in_cm = bot.ultrasound_measure()
   #         print(distance_in_cm)
    #        if distance_in_cm in (-1, -2):
     #           print('lol')
      #      elif distance_in_cm > 1:
       #         bot.right(255)
        #        bot.left(255)
         #       print('WHOA')
          #      music.stop()

