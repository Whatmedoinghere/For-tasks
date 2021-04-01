import RPi.GPIO as GPIO
import time
import gpiofunc

chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

input_Volt = 3,26

value = input()

def num2dac ( value ):
    gpiofunc.lightNumber ( value )

num2dac ( value )

GPIO.cleanup ()