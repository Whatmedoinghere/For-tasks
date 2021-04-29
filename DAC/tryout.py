import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
 

chan_list = (26, 19, 13, 6, 5, 11, 9, 10)
GPIO.setmode (GPIO.BCM)
GPIO.setup (chan_list, GPIO.OUT)

def decToBinList( decNumber ) :
    vector = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range (0, 8) :
        if (decNumber % 2) == 1 :
            vector [i] = 1
        decNumber = decNumber // 2

        if decNumber == 0 :
            return vector
 
def num2dac ( value , samplingfrequency):
    GPIO.output (chan_list, 0)
    vector = decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)
    time.sleep (1/samplingfrequency)


GPIO.output (chan_list, 0)
GPIO.cleanup (chan_list)