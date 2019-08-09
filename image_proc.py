# all image proecessing will happen here.

from PIL import Image #, ImageGrab # uncomment on Windows
from pytesseract import image_to_string
import numpy as np
from numpy import matrix
import time

# linux only imports

import pyscreenshot as ImageGrab

#print(image_to_string(Image.open('just_name.png')))


# @param state is the which state it is taking the ss, start for before it swipes
def get_pic(state):
    print("starting")
    #im = ImageGrab.grab(bbox=(58,536,266,613)) # windows machine
    im = ImageGrab.grab(bbox=(843, 383, 981, 497)
        ,childprocess=False) # linux machine
    print("taken")
    im.save('screenshots/user_{}.png'.format(state))

def average_image_color(filename):
	i = Image.open(filename)
	h = i.histogram()

	# split into red, green, blue
	r = h[0:256]
	g = h[256:256*2]
	b = h[256*2: 256*3]

	# perform the weighted average of each channel:
	# the *index* is the channel value, and the *value* is its weight
	return (
		sum( i*w for i, w in enumerate(r) ) / sum(r),
		sum( i*w for i, w in enumerate(g) ) / sum(g),
		sum( i*w for i, w in enumerate(b) ) / sum(b)
	)

def return_avgs():
    l = matrix(average_image_color('screenshots/user_start.png'))
    d = matrix(average_image_color('screenshots/user_now.png'))
    return np.mean(l-d)
