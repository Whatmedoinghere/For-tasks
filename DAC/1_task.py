import RPi.GPIO as GPIO
import time
import gpiofunc

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

GPIO.output (chan_list, 0)

def num2dac ( value ):
    GPIO.output (chan_list, 0)
    vector = gpiofunc.decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)

try:

    flag = 1

    while flag == 1:
        print("input a number:")

        value = int(input())

        num2dac( value )

        print("type 1 to another input number")

        flag = int(input())

except ValueError:
    print("You did not type a number")


except Exception:
    print("You done something wrong")

finally:

    GPIO.output (chan_list, 0)

    GPIO.cleanup ()