# PiLEDcontrol
Python scripts to control simple LED lights using a raspberry pi running Pi OS Lite.

Made by Roy Wink

## color.py

This is a script made to quickly set the LED lights to a single color. Upon launch, a dictionary is shown with pre-set colors. As input, the user can either give one of those (exact) colors, or a seperate RGB list. For the latter, the input must be formulated as `[int_red, int_green, int_blue]`. All values must be integers between (and including) 0 and 255, with 255 resulting in maximum amperage through the lights.

The program can be terminated by giving `close` as input. This will also shut off the LEDs. To terminate the program without shutting the LEDS, `close-on` can be given as input.

## fading.py

`speed <int>`
`quick`

## randomBPM.py

`bpm <int>`
