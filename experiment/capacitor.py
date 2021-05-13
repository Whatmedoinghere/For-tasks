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

def num2pins (pins,  number ) :
    GPIO.output (pins , 0)
    vector = decToBinList (number)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (pins [7 - i], 1)


def adc ():
        N = 7
        middle = 128

        while N > 0:
            num2pins(DAC_list ,middle )
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

    while adc () > 1:
        print(adc (), "the capacitor was precharched, decharging")
        time.sleep(0.5)

    t_start = time.time()

    GPIO.output (capac_num, 1)

    while True:
        digit_volt = adc()
        num2pins (LEDS_list, digit_volt)
        if ( digit_volt ) < 250:
            listVolt.append(digit_volt)
            listTime.append(time.time() - t_start)
        else:
            break


    GPIO.output (capac_num, 0)
    
    while True:
        digit_volt = adc()
        num2pins (LEDS_list, digit_volt)
        if ( digit_volt ) > 1:
            listVolt.append(digit_volt)
            listTime.append(time.time() - t_start)
        else:
            break

    t_stop = time.time() - t_start

    plt.plot(listTime, listVolt)
    plt.title('Напряжение при зарядки и разрядке конденсатора')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.show()

    print("Напишите 1 если вас устраивает увиденное")

    flag = int(input())

    if (flag == 1):

        np.savetxt('data.txt', listVolt, fmt = '%3.0d')

        print("Writing value in data.txt, settings.txt")

        measure_amount = len(listVolt)
        
        print("measure amount = ", measure_amount, "t_stop = ", t_stop)


        dT = t_stop / measure_amount

        dV = maxVolt / 250

        setting = [dT, dV]

        np.savetxt('settings.txt', setting, fmt = '%5.4f')



except Exception():
    print ("Smth gone wrong")

finally:
    GPIO.output (LEDS_list, 0)
    GPIO.output (DAC_list, 0)
    GPIO.output (capac_num, 0)
    GPIO.cleanup ()