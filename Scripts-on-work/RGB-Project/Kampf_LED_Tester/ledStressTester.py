from re import S
import time, math
from timeit import repeat
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 200       # Number of LED pixels.
LED_PIN_WS1 = 18          # GPIO pin connected to the pixels (18 uses PWM!).                        WS1 connected to PI Zero Pin12
LED_PIN_WS2 = 12          # GPIO pin connected to the pixels (12 uses PWM!).                        WS2 connected to PI Zero Pin32
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


    
def orangeWipe():
        colorWipe(strip_ws1, strip_ws2, Color(255, 153, 51), 0)    # orange wipe
        time.sleep(5)
        colorWipe(strip_ws1, strip_ws2,Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def yellowWipe():
        colorWipe(strip_ws1, strip_ws2, Color(255, 255, 0), 0)     # yellow wipe
        time.sleep(5)
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def greenWipe():
        colorWipe(strip_ws1, strip_ws2, Color(0, 255, 0), 0)       # Green wipe
        time.sleep(5)
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def blueWipe():
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 255), 0)       # Blue wipe
        time.sleep(5)
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def CyanWipe():
        colorWipe(strip_ws1, strip_ws2, Color(0, 255, 255), 0)     # Cyan wipe
        time.sleep(5)
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def PinkWipe():
        colorWipe(strip_ws1, strip_ws2, Color(255, 0, 255), 0)     # Pink Wipe 
        time.sleep(5)   
        colorWipe(strip_ws1, strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe

def showWS1():
        colorWipe(strip_ws1, Color(255, 0, 255), 0) # Pink Wipe 
        time.sleep(5)   
        colorWipe(strip_ws1, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe
   
def showWS2():
        colorWipe( strip_ws2, Color(255, 0, 255), 0) # Pink Wipe 
        time.sleep(5)   
        colorWipe( strip_ws2, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe




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
    
    
def colorWipe(strip, color, wait_ms=50):
    print("starting colorWipe animation")
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)  #Funktion rpi_ws281x.color wandelt DEC in BIN  um
        strip.show()
        time.sleep(wait_ms / 1000.0)


def terminateSequence():
    colorWipe(strip_ws1, Color(255, 255, 255, 255), 0)  # Composite White + White LED wipe
    colorWipe(strip_ws1, Color(0, 0, 0, 0), 0)  # Composite White + White LED wipe
            
                   

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    strip_ws1 = PixelStrip(LED_COUNT, LED_PIN_WS1, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)       #WS1 Strip Init
    strip_ws2 = PixelStrip(LED_COUNT, LED_PIN_WS2, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)       #Ws2 Strip init 

    strip_ws1.begin()
    strip_ws2.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            #show WS1 and WS2 and test them for any common mistakes
            orangeWipe(strip_ws1, strip_ws2)
            time.sleep(15)
            greenWipe(strip_ws1, strip_ws2)
            time.sleep(15)
            blueWipe(strip_ws1, strip_ws2)
            time.sleep(10)
            #Show Message to operator show them WS1, wait 5sec then show WS2 to clearify right cablelling
            showWS1(strip_ws1)
            time.sleep(5)
            showWS2(strip_ws2)

    except KeyboardInterrupt:
        if args.clear:
            terminateSequence()

    except SystemExit:
        terminateSequence()