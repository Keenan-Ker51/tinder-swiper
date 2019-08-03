from pynput.keyboard import Key, Controller
import time
import random

swiper = Controller()

while True:
    time.sleep((random.randint(1,10)/10)+1)
    for x in range (random.randint(3,5)):
        swiper.press(Key.space)
        swiper.release(Key.space)
        time.sleep(0.3)
    swiper.press(Key.right)
    time.sleep(0.2)
    swiper.release(Key.right)
