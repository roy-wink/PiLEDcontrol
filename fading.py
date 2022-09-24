# script to set a fading show, with depending speed
# author: Roy Wink, sep 2022

import re
import threading
import pigpio
pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# choose debugging options
debug = False

# get speed (1 - 100)
# todo: get try for instance and allow over 100 with confirm
speed = 0
while speed > 100 or speed <= 0:
    speed = float(input('Input the desired speed on a scale of 1 to 100:\n $ '))

global step
step = speed / 100

# while true argument
global stopping
stopping = False

def updateColor(color, step):
    color += step

    if color > 255:
        return 255
    if color < 0:
        return 0

    return color
    
def setLight(pin, color):
    if debug:
        print('setting %s to %f' % (pin, color))
    pi.set_PWM_dutycycle(pin, color)

def threadingFunc():
    stop_arg = input('\nGive an input to stop fading\n $ ')

    # elevate variables
    global step
    global stopping

    # check for the hidden speed change
    expr = 'speed \d?\.?\d+'
    check = re.search(expr, stop_arg)
    if check:
        speed = float(stop_arg.split(' ')[1])
        step = speed / 100
        print('speed adjusted')

        # reset threading
        x = threading.Thread(target=threadingFunc)
        x.start()

    # check for quick termination
    elif stop_arg == 'quick':
        stopping = True
        step = 10

    # else, just stop
    elif stop_arg != '':
        stopping = True
        print('program will terminate after this loop')

# set starting position
red = 255
green = 0
blue = 0

setLight(RED_PIN, red)
setLight(GREEN_PIN, green)
setLight(BLUE_PIN, blue)

# set up threading for input to stop
x = threading.Thread(target=threadingFunc)
x.start()

# start fading loop; stop when stopping is raised
while not stopping:
    # add green to red
    while green < 255:
        green = updateColor(green, step)
        setLight(GREEN_PIN, green)
    
    # remove red from green
    while red > 0:
        red = updateColor(red, -step)
        setLight(RED_PIN, red)
    
    # add blue to green
    while blue < 255:
        blue = updateColor(blue, step)
        setLight(BLUE_PIN, blue)
    
    # remove green from blue
    while green > 0:
        green = updateColor(green, -step)
        setLight(GREEN_PIN, green)
    
    # add red to blue
    while red < 255:
        red = updateColor(red, step)
        setLight(RED_PIN, red)
    
    # remove blue from red
    while blue > 0:
        blue = updateColor(blue, -step)
        setLight(BLUE_PIN, blue)

setLight(RED_PIN, 0)
print('terminated')
