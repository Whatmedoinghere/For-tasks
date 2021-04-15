import RPi.GPIO as GPIO
import time
import gpiofunc


chan_list = [26, 19, 13, 6, 5, 11, 9, 10]

sound_list = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode (GPIO.BCM)

GPIO.setup   (chan_list, GPIO.OUT)

GPIO.setup   (sound_list, GPIO.OUT)

GPIO.output (chan_list, 0)

GPIO.output (sound_list, 0)

GPIO.setup (4, GPIO.IN)

GPIO.setup   (17, GPIO.OUT)

GPIO.output (17, 1)


def num2dac ( value ):
    GPIO.output (chan_list, 0)
    vector = gpiofunc.decToBinList (value)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (chan_list [7 - i], 1)

def num2sound ( value ):
    GPIO.output (sound_list, 0)

    for i in range (0, 8) :
        if (middle > i * 255 / 8):
            GPIO.output (sound_list [7 - i], 1)

            


    


try:

    while True:
        N = 7
        middle = 128

        while N > 0:
            num2dac( middle )
            time.sleep(0.001)

            if GPIO.input(4) == 0 :
                middle -= 2**(N - 1)
            else:
                middle += 2**(N-1)
            N -= 1           
                    
        middle -= 1
        middle = int(middle)
        print ("Digital value:", int(middle), "Analog value:", middle * 3.3 / 255)

        num2sound ( middle )



    
    


except Exception:
    print("You done something wrong")

finally:    
    GPIO.output (chan_list, 0)
    GPIO.output (17, 0)
    GPIO.output (sound_list, 0)
    GPIO.cleanup ()