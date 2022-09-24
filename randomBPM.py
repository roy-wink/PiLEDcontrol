# script for randomly set colors with a set bpm

import re
import time
import random
import threading
import pigpio
pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# choose debugging options
debug = False

bpm = 0
while bpm <= 0:
    bpm = input('\nGive a BPM to change colors on\n $ ')
    try:
        bpm = int(bpm)
    except ValueError or TypeError:
        print('\n\tunknown input: %s. please anter a integer.' % bpm)
        bpm = 0

global wait_time
wait_time = 1 / (bpm / 60)

# while true argument
global stopping
stopping = False

def threadingFunc():
    stop_arg = input('Give an input to kill application\n $ ')
    
    # elevate variables
    global wait_time
    global stopping
    
    # check for the hidden speed change
    expr = 'bpm\s\d+[^.]'
    check = re.search(expr, stop_arg)
    if check:
        new_bpm = int(stop_arg.split(' ')[1])
        if new_bpm > 0:
            wait_time = 1 / (new_bpm / 60)
            print('BPM adjusted')
        else:
            print('BPM of 0 is quite impossible...\n')
        
        # reset threading
        x = threading.Thread(target=threadingFunc)
        x.start()
    
    # else, just stop
    elif stop_arg != '':
        stopping = True
        print('program will terminate')

def setLight(red, green, blue):
    if debug:
        print('setting lights to [%i, %i, %i]' % (red, green, blue))
    
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(GREEN_PIN, green)
    pi.set_PWM_dutycycle(BLUE_PIN, blue)

# set up threading for input to stop
x = threading.Thread(target=threadingFunc)
x.start()

while not stopping:
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    setLight(red, green, blue)
    
    time.sleep(wait_time)

setLight(0, 0, 0)
