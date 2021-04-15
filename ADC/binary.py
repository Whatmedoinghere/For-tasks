

x = int(input())

left  = 0
right = 128

def binary(left, right):
    while True:
        if right > x:
            right = (right + left) / 2
        else:
            if right - left < 1:
                break 
            else:
                left = right
                right = right * 2

    right = int(right + 0.5)
    print(right)

binary(left, right)