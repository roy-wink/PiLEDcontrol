# Script to set a fading light as alarm at a set time.

import numpy as np
import schedule
import time

# PIGPIO SETTINGS -------------------------------------------------------------
import pigpio
pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

# SET ALARM HERE --------------------------------------------------------------
alarm_time = '19:56'
off_time = '19:57'
fade_time = 30
steps = 100

final_color = [255, 0, 0]

def set_lights(color_list):
    red, green, blue = color_list
    
    pi.set_PWM_dutycycle(RED_PIN, red)
    pi.set_PWM_dutycycle(GREEN_PIN, green)
    pi.set_PWM_dutycycle(BLUE_PIN, blue)
    
    return None

def debug(color_list):
    print(color_list)
    
    return None

def run_alarm(fade_time, steps, final_color):
    for step in range(steps + 1)[1:]:
        this_color = np.multiply(final_color, (step / steps))
        set_lights(this_color)
        time.sleep(fade_time / steps)
        
    return None

def shutdown():
    off = [0, 0, 0]
    set_lights(off)

# SET UP ALARM ----------------------------------------------------------------
schedule.every().day.at(alarm_time).do(run_alarm, fade_time, steps, final_color)
schedule.every().day.at(alarm_time).do(shutdown)

while True:
    schedule.run_pending()
    time.sleep(30)
