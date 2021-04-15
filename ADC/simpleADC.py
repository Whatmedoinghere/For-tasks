import RPi.GPIO as GPIO
import time
import gpiofunc


chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

GPIO.output (chan_list, 0)

GPIO.setup (4, GPIO.IN)

GPIO.setup   (17, GPIO.OUT)

GPIO.output (17, 1)


def num2dac ( value ):
    GPIO.output (chan_list, 0)
    vector = gpiofunc.decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)


try:

    while True:
        i = 0

        while True:
            num2dac(i)
            time.sleep(0.001)
            if GPIO.input(4) == 0 :
                break
            else :
                i += 1
            
        print ("Digital value:", i, "Analog value:", i * 3.3 / 255)
    


except Exception:
    print("You done something wrong")

finally:    
    GPIO.output (chan_list, 0)
    GPIO.output (17, 0)
    GPIO.cleanup ()