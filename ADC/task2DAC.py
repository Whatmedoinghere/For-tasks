import RPi.GPIO as GPIO
import time
import gpiofunc

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

GPIO.output (chan_list, 0)

try:

    print("input number of repetitions:")

    repetitionsNumber = int(input())

    for i in range (0, repetitionsNumber):
        for j in range (0, 256):
            gpiofunc.lightNumber(j)

except ValueError:
    print("You did not type a number")

except Exception:
    print("You done something wrong")

finally:
    GPIO.output (chan_list, 0)

    GPIO.cleanup ()