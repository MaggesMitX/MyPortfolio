#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 650       # Number of LED pixels.
LED_PIN = 21          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN_2 = 12        # GPIO pin connected to the pixels (12 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 180  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



def colorWipe(strip, color, wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def WS1():
    pass
def WS2():
    pass

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    #Create NeoPixel object for second pin
    strip2 = PixelStrip(LED_COUNT, LED_PIN_2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    strip2.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

try:

        while True:
            print("red")
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip2, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 0, 0), 5)
            colorWipe(strip2, Color(0, 0, 0), 5)
            print("green")
            colorWipe(strip, Color(0, 255, 0))  # Green wipe
            colorWipe(strip2, Color(0, 255, 0))  # Green wipe
            colorWipe(strip, Color(0, 0, 0), 5)
            colorWipe(strip2, Color(0, 0, 0), 5)
            print("blue")
            colorWipe(strip, Color(0, 0, 255))  # Blue wipe
            colorWipe(strip2, Color(0, 0, 255))  # Blue wipe
            print("clearAll")
            colorWipe(strip, Color(0, 0, 0), 5)
            colorWipe(strip2, Color(0, 0, 0), 5)
            time.sleep(2)
            print("Show WS1 Wipe")
            colorWipe(strip, Color(0, 255, 0))  # Green wipe WS1
            print("clear WS1")
            colorWipe(strip, Color(0, 0, 0), 5) #clear leds
            print("Show WS2 Wipe")
            colorWipe(strip2, Color(0, 255, 0))  # Green wipe WS2
            colorWipe(strip2, Color(0, 0, 0), 5) #clear leds
            print("second wipe Ws2")
            colorWipe(strip2, Color(0, 255, 0))  # Green wipe WS2
            colorWipe(strip2, Color(0, 0, 0), 5) #clear leds

except KeyboardInterrupt:
    if args.clear:
        colorWipe(strip, Color(0, 0, 0), 5)
