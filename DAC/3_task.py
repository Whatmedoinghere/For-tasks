import RPi.GPIO as GPIO
import time
import gpiofunc
import numpy as np
import matplotlib.pyplot as plt
import math

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

GPIO.output (chan_list, 0)

Volt_amplitude = 3.256

Num_volt = 3.256/256


try:
    print ("Give the time of whole sin voltage")
    timenew = int(input())

    print ("Give the frequency")
    frequency =float(input())

    print ("Give the samoling frequency")
    samplingFrequency =float(input())


    timearray = np.arange(0, timenew, 1/frequency)
    amplitude = Volt_amplitude * np.sin(timearray - math.pi/2) / 2 + Volt_amplitude / 2
    plt.plot(timearray, amplitude)
    plt.title('Синус')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда sin(time)')
    plt.show()


    print ("Type 1 if sin graph satisfies you")

    flag = input()

    if flag == 1:
        newtime = np.arange(0, timenew, 1/samplingFrequency)
        for timerunner in newtime:
            gpiofunc.lightNumber_time( Num_volt * amplitude[newtime] , 1 / samplingFrequency)








except Exception:
    print("You done something wrong, or the coder is a moron")

finally:
    GPIO.output (chan_list, 0)

    GPIO.cleanup ()