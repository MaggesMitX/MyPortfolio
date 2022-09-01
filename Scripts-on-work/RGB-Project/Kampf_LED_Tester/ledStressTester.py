#!/usr/bin/env python3
import time
from rpi_ws281x import PixelStrip, Color
import argparse
from threading import Thread

# LED strip configuration:
LED_COUNT = 650       # Number of LED pixels.
LED_PIN = 21          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN_2 = 12        # GPIO pin connected to the pixels (12 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 180  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def init_colorWipe(strip, color, wait_ms=5):
    stripgl = strip
    print("starte F1")
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def init_colorWipe2(strip2, color, wait_ms=5):
    print("starte F2")
    """Wipe color across display a pixel at a time."""
    for i in range(strip2.numPixels()):
        strip2.setPixelColor(i, color)
        strip2.show()
        time.sleep(wait_ms / 1000.0)

def colorWipe():
    print("red wipe")
    init_colorWipe(strip, Color(255, 0, 0))
    init_colorWipe(strip, Color(0, 0, 0), 5)
    print("green")
    init_colorWipe(strip, Color(0, 255, 0))
    init_colorWipe(strip, Color(0, 0, 0), 5)

def colorWipe2():
    print("red wipe")
    init_colorWipe2(strip2, Color(255, 0, 0))
    init_colorWipe(strip, Color(0, 0, 0), 5)   
    print("green")
    init_colorWipe2(strip, Color(0, 255, 0))
    init_colorWipe2(strip, Color(0, 0, 0), 5)
    
def strobews1(strip, wait_ms=1000, strobe_count=1, pulse_count=1):
    from random import randrange
    "In strobe_count wird die Häufigkeit der Blitze eingestellt"
    "Die Variable pulse_count stellt die Wiederholung der Blitze ein. Die Zeit zwischen den Pulsen ist eine Zufallszahl zwischen 0 und 45 ms time.sleep(randrange(0,45,1)."
    for strobe in range(strobe_count):    
        for pulse in range(pulse_count):
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,255)
            strip.show()
            time.sleep(randrange(0,45,1)/1000.0)
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,0)
            strip.show()
        time.sleep(wait_ms/1000.0)

def strobews2(strip2, wait_ms=1000, strobe_count=1, pulse_count=2):
    from random import randrange
    "In strobe_count wird die Häufigkeit der Blitze eingestellt"
    "Die Variable pulse_count stellt die Wiederholung der Blitze ein. Die Zeit zwischen den Pulsen ist eine Zufallszahl zwischen 0 und 45 ms time.sleep(randrange(0,45,1)."
    for strobe in range(strobe_count):    
        for pulse in range(pulse_count):
            for i in range(strip2.numPixels()):
                strip2.setPixelColorRGB(i, 0,0,255)
            strip2.show()
            time.sleep(randrange(0,45,1)/1000.0)
            for i in range(strip2.numPixels()):
                strip2.setPixelColorRGB(i, 0,0,0)
            strip2.show()
        time.sleep(wait_ms/1000.0)      


threadCWipe_WS1 = Thread(target=colorWipe)
threadCWipe_WS2 = Thread(target=colorWipe2)
threadshowWS1 = Thread(target=strobews1)
threadshowWS2 = Thread(target=strobews2)

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


   
            threadCWipe_WS2(strip2, Color(0, 255, 0))
            print("clear green")
            threadCWipe_WS1(strip, Color(0, 0, 0), 5)
            threadCWipe_WS2(strip2, Color(0, 0, 0), 5)
            print("blue")
            threadCWipe_WS1(strip, Color(0, 0, 255))
            threadCWipe_WS2(strip2, Color(0, 0, 255))
            print("clear red")
            threadCWipe_WS1(strip, Color(0, 0, 0), 5)
            threadCWipe_WS2(strip2, Color(0, 0, 0), 5)
            print("show only WS1")
            time.sleep(3)
            threadshowWS1
            threadshowWS2
            time.sleep(3)
except KeyboardInterrupt:
    if args.clear:
        colorWipe(strip, Color(0, 0, 0), 5)