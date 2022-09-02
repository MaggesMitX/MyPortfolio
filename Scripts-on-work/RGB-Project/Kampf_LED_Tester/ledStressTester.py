#!/usr/bin/env python3
import argparse
import threading
import time
from threading import Thread
from rpi_ws281x import Color, PixelStrip

# LED strip configuration:
LED_COUNT = 50       # Number of LED pixels.
LED_PIN = 21          # GPIO pin connected to the pixels (18 uses PWM!).
LED_PIN_2 = 12        # GPIO pin connected to the pixels (12 uses PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 180  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

#init ColorWipe Funtion for WS1 and WS2
def init_colorWipe(strip, color, wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def init_colorWipe2(strip2, color, wait_ms=5):
    """Wipe color across display a pixel at a time."""
    for i in range(strip2.numPixels()):
        strip2.setPixelColor(i, color)
        strip2.show()
        time.sleep(wait_ms / 1000.0)

#call ColorWipe function and declare colors 
def showcolorWipe(strip):
    print("Showing WS1 red wipe")
    init_colorWipe(strip, Color(255, 0, 0))
    time.sleep(3)
    init_colorWipe(strip, Color(0, 0, 0), 5)
    time.sleep(0.5)
    print("Showing WS1 green wipe")
    init_colorWipe(strip, Color(0, 255, 0))
    time.sleep(3)
    init_colorWipe(strip, Color(0, 0, 0), 5)
    time.sleep(0.5)
    print("Showing WS1 blue wipe")
    init_colorWipe(strip, Color(0, 0, 255))
    time.sleep(3)
    init_colorWipe(strip, Color(0, 0, 0), 5)
    time.sleep(0.5)
    print("Clear all LEDs from WS1....")

def showcolorWipe2(strip2):
    print("Showing WS2 red wipe")
    init_colorWipe2(strip2, Color(255, 0, 0))
    time.sleep(3)
    init_colorWipe2(strip2, Color(0, 0, 0), 5)
    time.sleep(0.5)   
    print("Showing WS2 green wipe")
    init_colorWipe2(strip2, Color(0, 255, 0))
    time.sleep(3)
    init_colorWipe2(strip2, Color(0, 0, 0), 5)
    time.sleep(0.5)
    print("Showing WS2 blue wipe")
    init_colorWipe2(strip2, Color(0, 0, 255))
    time.sleep(3)
    init_colorWipe2(strip2, Color(0, 0, 0), 5)
    time.sleep(0.5)
    print("Clear all LEDs from WS2....")

#Init strobe function for WS1 and WS2
def strobews1(strip, wait_ms=1000, strobe_count=1, pulse_count=1):
    from random import randrange
    "In strobe_count wird die Häufigkeit der Blitze eingestellt"
    "Die Variable pulse_count stellt die Wiederholung der Blitze ein. Die Zeit zwischen den Pulsen ist eine Zufallszahl zwischen 0 und 45 ms time.sleep(randrange(0,45,1)."
    for strobe in range(strobe_count):    
        for pulse in range(pulse_count):
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,255)
            strip.show()
            time.sleep(2)
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,0)
            strip.show()
        time.sleep(1)

def strobews2(strip2, wait_ms=1000, strobe_count=1, pulse_count=2):
    from random import randrange
    "In strobe_count wird die Häufigkeit der Blitze eingestellt"
    "Die Variable pulse_count stellt die Wiederholung der Blitze ein. Die Zeit zwischen den Pulsen ist eine Zufallszahl zwischen 0 und 45 ms time.sleep(randrange(0,45,1)."
    for strobe in range(strobe_count):    
        for pulse in range(pulse_count):
            for i in range(strip2.numPixels()):
                strip2.setPixelColorRGB(i, 0,0,255)
            strip2.show()
            time.sleep(2)
            for i in range(strip2.numPixels()):
                strip2.setPixelColorRGB(i, 0,0,0)
            strip2.show()
        time.sleep(1)      


print("Booting functions...")
time.sleep(2)
# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    c    = 0
    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    #Create NeoPixel object for second pin
    strip2 = PixelStrip(LED_COUNT, LED_PIN_2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    #creating threads for sync run of both winding sides
    tCWipe_WS1 = threading.Thread(target=showcolorWipe, args=(strip,))
    tCWipe_WS2 = Thread(target=showcolorWipe2, args=(strip2,))
    tshowWS1 = Thread(target=strobews1, args=(strip,))
    tshowWS2 = Thread(target=strobews2, args=(strip2,))
    print("Initialize Main Loop and stripes...")
    strip.begin()
    strip2.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

try:
    print("starting LED tester.py | Checking Winding Sides with threads..")
    print("Start checking threads..")
    time.sleep(1)
    print("Check complete..starting threads!")
    #starting threads with"start" function
    tCWipe_WS1.start()
    tCWipe_WS2.start()
    #with "join" the threads will stop an come back to main
    tCWipe_WS1.join()
    tCWipe_WS2.join()
    print("ColorWipe finished, close threads..")
    time.sleep(3)
    print("Done!, load and show with blinking the Winding Side 1 and Winding Side 2..")
    tshowWS1.start()
    tshowWS2.start()
    #with "join" the threads will stop an come back to main
    time.sleep(5)
    tshowWS1.join()
    tshowWS2.join()
    print("show WS1 and WS2 threads finished, closing threads..")
    time.sleep(2)
    print("Done! closing programm..")
    init_colorWipe(strip, Color(0, 0, 0), 5)
    init_colorWipe2(strip2, Color(0, 0, 0), 5)
    time.sleep(1)

except KeyboardInterrupt:
    if args.clear:
        print("Aborting program...clear LEDs..")
        init_colorWipe(strip, Color(0, 0, 0), 5)
        init_colorWipe2(strip2, Color(0, 0, 0), 5)
