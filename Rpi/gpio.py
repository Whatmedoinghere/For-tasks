import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup   (chan_list, GPIO.OUT)



def lightUp( ledNumber, period ) :
    GPIO.output  (chan_list [ledNumber], 1)
    time.sleep   (period)
    GPIO.output  (chan_list [ledNumber], 0)

def blink( ledNumber, blinkCount, blinkPeriod ) :
    for i in range (0, blinkCount):
        lightUp (ledNumber, blinkPeriod)
        time.sleep (blinkPeriod)

def runningLight( count, period ) :
    for i in range (0, count) :
        for j in range (0, 8) :
            lightUp (j, period)

def runningDark( count, period ) :
    GPIO.output (chan_list, 1)

    for i in range (0, count) :
        for j in range (0, 8) :
            GPIO.output (chan_list[j]    , 0)
            GPIO.output (chan_list[(j + 7) % 8], 1)
            time.sleep  (period)

    GPIO.output (chan_list, 0)

def decToBinList( decNumber ) :
    vector = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range (0, 8) :
        if (decNumber % 2) == 1 :
            vector [i] = 1
        decNumber = decNumber // 2

        if decNumber == 0 :
            return vector
    
    return vector

def lightNumber( number ) :
    vector = decToBinList (number)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)

    time.sleep (2)
    GPIO.output (chan_list, 0)

def runningPattern( pattern, direction ) :
    vector = decToBinList (pattern)

    for i in range (0, 9) :
        for j in range (0, 8) :
            if vector[(i + j) % 8] == 1 :
                GPIO.output (chan_list [7 - j], 1)

        time.sleep (0.5)
        GPIO.output (chan_list, 0)

def SHIM( period ) :
    gpioPWM.ChangeDutyCycle (0)

    for i in range (0, 100, 5) :
        gpioPWM.ChangeDutyCycle (i)
        time.sleep(period * 5 / 100)

    for i in range (100, -5, -5) :
        gpioPWM.ChangeDutyCycle (i)
        time.sleep(period * 5 / 100)

# lightUp (3, 2)

# blink (4, 10, 0.1)

# runningLight (3, 0.2)

# runningDark (3, 0.3)

#lightNumber (128 + 4 + 1)

# runningPattern (128 + 4 + 1, 1)

#SHIM(3)

#gpioPWM.stop ()

GPIO.output (chan_list, 0)

GPIO.cleanup ()