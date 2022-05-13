import time, math
from timeit import repeat
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 200       # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


    
def orangeWipe():
        colorWipe(strip, Color(255, 153, 51), 0)    # orange wipe
def yellowWipe():
        colorWipe(strip, Color(255, 255, 0), 0)     # yellow wipe
def greenWipe():
        colorWipe(strip, Color(0, 255, 0), 0)       # Green wipe
def blueWipe():
        colorWipe(strip, Color(0, 0, 255), 0)       # Blue wipe    
def CyanWipe():
        colorWipe(strip, Color(0, 255, 255), 0)     # Cyan wipe
def PinkWipe():
        colorWipe(strip, Color(255, 0, 255), 0)     # Pink Wipe    
    

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)
     

def pulsing_light(strip, wait_ms=50, iterations=10):
    print("starting Pulsing Light animation")
    """Helle LIchteffekte in Kette"""
    position = 0
    for i in range(strip.numPixels() * 2):
        position = position+1
        for j in range(strip.numPixels()):
            strip.setPixelColor(j,Color(round(((math.sin(j+position) * 127 + 128)/255)*255),round(((math.sin(j+position) * 127 + 128) /255)*100), round(((math.sin(j+position) * 127 + 128) /255)*100)))
        strip.show()
        time.sleep(wait_ms/1000.0)
        
            

def strobe(strip, wait_ms=400, strobe_count=7, pulse_count=12):
    from random import randrange
    """LED als springender Ball"""
    for strobe in range(strobe_count):    
        for pulse in range(pulse_count):
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 255,255,255)
            strip.show()
            time.sleep(randrange(0,45,1)/1000.0)
            for i in range(strip.numPixels()):
                strip.setPixelColorRGB(i, 0,0,0)
            strip.show()
        time.sleep(wait_ms/1000.0)


def bouncing_balls(strip,ball_count=4, wait_ms=200):

    start_time = time.time()
    ClockTimeSinceLastBounce = [0 for i in range(ball_count)]
    StartHeight=1

    for i in range(ball_count):
        ClockTimeSinceLastBounce[i] = time.time()
    
    Height = [0 for i in range(ball_count)]
    Position = [0 for i in range(ball_count)]
    ImpactVelocity = [0 for i in range(ball_count)]
    ImpactVelocityStart= math.sqrt(-2 * -9.81 * 1)
    Dampening = [0 for i in range(ball_count)]
    TimeSinceLastBounce = [0 for i in range(ball_count)]

    for i in range(0,ball_count,1):
        last_ClockTimeSinceLastBounce = ClockTimeSinceLastBounce[i]
        ClockTimeSinceLastBounce[i] = time.time() - last_ClockTimeSinceLastBounce

        Height[i] = StartHeight
        Position[i] = 0
        ImpactVelocity[i] = math.sqrt(-2 * -9.81 * 1)
        TimeSinceLastBounce[i] = 0
        Dampening[i] = 0.90 - (float(i)/(ball_count**2))

    while True:
        for i in range(ball_count):
            TimeSinceLastBounce[i] = time.time() - ClockTimeSinceLastBounce[i]
            Height[i] = 0.5 * (-9.81) * (TimeSinceLastBounce[i]**2) + ImpactVelocity[i] * TimeSinceLastBounce[i]
            if (Height[i] < 0):
                Height[i] = 0
                ImpactVelocity[i] = Dampening[i] * ImpactVelocity[i]
                ClockTimeSinceLastBounce[i] = time.time()
                if (ImpactVelocity[i] < 0.01):
                    ImpactVelocity[i] = ImpactVelocityStart
                                  
            Position[i] = round(Height[i] * (strip.numPixels()-1)/StartHeight)   #Hier wird die relative Höhe auf die absolute Höhe mit der LED Anzahl umgewandelt.
        for i in range(ball_count):
            strip.setPixelColorRGB(Position[i], 0, 0,255)    
        strip.show()
        for i in range(strip.numPixels()):
            strip.setPixelColorRGB(i, 0,0,0)
            
def snow_sparkle(strip,sparkle_delay=20):
    from random import randint
    pixel= randint(0,strip.numPixels())
    speed_delay=randint(100,1000)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0x10,0x10,0x10))
    strip.show()
    time.sleep(speed_delay/1000.0)
    strip.setPixelColorRGB(pixel, 255,255,255)
    strip.show()
    time.sleep(sparkle_delay/1000.0)
    
    
def colorWipe(strip, color, wait_ms=50):
    print("starting colorWipe animation")
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)  #Funktion rpi_ws281x.color wandelt DEC in BIN  um
        strip.show()
        time.sleep(wait_ms / 1000.0)
        
def rainbow(strip, wait_ms=20, iterations=1):
    print("starting rainbow animation")
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


        
def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)

def terminateSequence():
    colorWipe(strip, Color(255, 255, 255, 255), 0)  # Composite White + White LED wipe
    colorWipe(strip, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe
            
                   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            #LED Strip Programme(
            #colorWipe(strip, color)
            #theaterChase(strip)
            orangeWipe(strip)
            #theaterChaseRainbow(strip)
            #pulsing_light(strip)
            #snow_sparkle(strip)
            #strobe(strip)
            #bouncing_balls(strip)
            #colorWipe(strip, Color(255, 0, 0), 0)  # Red wipe
            #time.sleep(2)
            #colorWipe(strip, Color(0, 255, 0), 0)  # Blue wipe
            #time.sleep(2)
            #colorWipe(strip, Color(0, 0, 255), 0)  # Green wipe
            #time.sleep(2)
            
    except KeyboardInterrupt:
        if args.clear:
            terminateSequence()

    except SystemExit:
        terminateSequence()