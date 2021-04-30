import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt

capac_num = 17

maxVolt = 3.3

Comparator = 4

DAC_list = (26, 19, 13, 6, 5, 11, 9, 10)

LEDS_list = (21, 20, 16, 12, 7, 8, 25, 24)

GPIO.setmode (GPIO.BCM)

GPIO.setup   (DAC_list, GPIO.OUT)
GPIO.setup   (LEDS_list, GPIO.OUT)

GPIO.output (DAC_list, 0)
GPIO.output (LEDS_list, 0)

GPIO.setup (Comparator, GPIO.IN)

GPIO.setup   (capac_num, GPIO.OUT)

def decToBinList( decNumber ) :
    vector = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range (0, 8) :
        if (decNumber % 2) == 1 :
            vector [i] = 1
        decNumber = decNumber // 2

        if decNumber == 0 :
            return vector
    
    return vector

def num2leds ( number ) :
    GPIO.output (LEDS_list , 0)
    vector = decToBinList (number)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (LEDS_list [7 - i], 1)

def num2dac ( value ):
    GPIO.output (DAC_list, 0)
    vector = gpiofunc.decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (DAC_list [7 - i], 1)


def adc ():
        N = 7
        middle = 128

        while N > 0:
            num2dac( middle )
            time.sleep(0.001)

            if GPIO.input(Comparator) == 0 :
                middle -= 2**(N - 1)
            else:
                middle += 2**(N - 1)
            N -= 1

        return middle



try:
    
    listVolt = []
    listTime = []

    GPIO.output (capac_num, 0)

    while adc () > 0:
        time.sleep(0.5)

    t_start = time.time()

    GPIO.output (capac_num, 1)

    while True:
        digit_volt = adc()
        if ( digit_volt ) < 240:
            listVolt.append(digit_volt * maxVolt / 255)
            listTime.append(time.time - t_start)
        else:
            break


    GPIO.output (capac_num, 0)
    
    while True:
        digit_volt = adc()
        if ( digit_volt ) > 0:
            listVolt.append(digit_volt * maxVolt / 255)
            listTime.append(time.time - t_start)
        else:
            break

    t_stop = time.time()

    plt.plot(time, amplitude)
    plt.title('Напряжение при зарядки и разрядке конденсатора')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.show()

    np.savetxt('data.txt', listVolt, fmt = '%d')

    measure_amount = np.len(listTime)

    dT = t_stop / measure_amount

    dV = maxVolt / 255

    np.savetxt('settings', dT, dV, fmt = '%d')



except Exception():
    print ("Smth gone wrong")

finally:

    GPIO.output (LEDS_list, 0)
    GPIO.output (DAC_list, 0)
    GPIO.output (capac_num, 0)
    GPIO.cleanup ()