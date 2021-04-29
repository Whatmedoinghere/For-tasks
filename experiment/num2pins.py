def num2pins (pins,  number ) :
    GPIO.output (pins , 0)
    vector = decToBinList (number)

    for i in range (0, 8) :
        if vector[i] == 1 :
            GPIO.output (pins [7 - i], 1)