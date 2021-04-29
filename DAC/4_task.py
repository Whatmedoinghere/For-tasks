import RPi.GPIO as GPIO
import time
import numpy as np
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io

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

data_dir = pjoin('/home', 'student', 'Desktop')
wav_fname = pjoin(data_dir, 'SOUND.WAV')
samplerate, data = wavfile.read(wav_fname)
length = data.shape[0] / samplerate

print ("продолжительность: ", int(length), "s, количество каналов: ", data.shape[1], ", частота: ", samplerate, ", data type: ", type (data[1, 0]))

array = int((data[:, 0] + 32768) / 256)

try:
    for i in array:
        num2dac (int(i))
except ValueError:
    print ("Ошибка в в размере входных данных. Выходим из программы")
except:
    print ("Неизвестная ошибка. Выходим из программы")
finally:
    GPIO.output (chan_list, 0)
    GPIO.cleanup (chan_list)