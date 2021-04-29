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
 
def num2dac ( value ):
    GPIO.output (chan_list, 0)
    vector = decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)

try:
    worktime = 0
    frequency = 0
    samplingFrequency = 0


    worktime = int(input ("Введите время работы: "))
    frequency = int(input ("Введите частоту синусоидального сигнала: "))        
    samplingFrequency = int(input ("Введите частоту сэмплироания: "))



    freqarr = np.arange(0, worktime, 1/samplingFrequency)
    ndarray = np.int32(np.round(127.5 - 127.5*np.cos(2 * np.pi * frequency * freqarr)))
    plt.plot(freqarr, ndarray)
    plt.title('Подаваемый сигнал')
    plt.xlabel('Время')
    plt.ylabel('Амплитуда сигнала')
    plt.show()

    print("Напишите 1 если вас устраивает увиденное")

    flag = int(input())

    if flag == 1:
        for j in ndarray:
            num2dac (j)
            time.sleep (1 / samplingFrequency)
        
except Exception:
    print("Некая ошибка, выходим из программы.")
finally:
    GPIO.output (chan_list, 0)
    GPIO.cleanup (chan_list)
