# Simple script to set a single color

import pigpio
pi = pigpio.pi()

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

color_dictionary = {'off': [0, 0, 0],
                    'red': [255, 0, 0],
                    'green': [0, 255, 0],
                    'blue': [0, 0, 255],
                    'orange': [255, 31, 0],
                    'aqua': [0, 255, 255],
                    'purple': [255, 0, 255]
                    }

termination_argument = 'close'

def set_colors(color_list):
    red, green, blue = color_list
    
    print('setting color list [%i, %i, %i]' % (red, green, blue))

    # pi.set_PWM_dutycycle(RED_PIN, red)
    # pi.set_PWM_dutycycle(GREEN_PIN, green)
    # pi.set_PWM_dutycycle(BLUE_PIN, blue)
    
    print('succesfull.')
    return True


close_application = False
while not close_application:
    # explain input options
    print('\ncolors currently in the dictionary:\n')
    for key in color_dictionary:
        print(key)

    color_input = input('either enter a color from the list, or a specific list as [r, g, b] \nenter \"%s\" to terminate the program\n\n$ ' % termination_argument)
    
    # check for rgb list and convert
    if color_input[0] == '[' and color_input[-1] == ']':
        color_input = color_input[1:-1].split(',')
        color_list = []
        for color in color_input:
            color_list.append(int(color))
        set_colors(color_list)
        continue
    
    # check for input from dictionary
    if color_input in color_dictionary:
        set_colors(color_dictionary[color_input])
        continue
    
    # check for termination argument
    if color_input == termination_argument:
        close_application = True
        set_colors([0, 0, 0])
        print('Terminating application. Thank you')
        continue

    # ending up here means impropper input
    print('\n\t\tunknown input: %s' % color_input)