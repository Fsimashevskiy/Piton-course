import os
import math

clear = lambda: os.system('cls')
result = 0

def Calculate(a, b, number):
    if (number == 1):
        print("Result: " + str(a+b))
    if (number == 2):
        print("Result: " + str(a - b))
    if (number == 3):
        print("Result: " + str(a * b))
    if (number == 4):
        print("Result: " + str(a / b))
    if (number == 5):
        print("Result: " + str(math.ceil(a/b)))
    if (number == 6):
        print("Choose number: "
              "\n 1. " + str(a) + "\n 2. " + str(b))
        o = int(input())
        if (o == 1):
            print("Result " + str(math.sqrt(a)))
        else:
            print("Result " + str(math.sqrt(b)))
    if (number == 7):
        print("Result " + str(math.fmod(a, b)))
    if (number == 8):
        print("Choose number: ")
        c = float(input())
        Area = {
            'Per': (lambda a, b: 2*(a + b)),
            'Plo': (lambda a, b, c: 2*(a * b + b * c + a * c)),
        }
        print('Perimeter = ', Area['Per'](a, b))
        print('Area = ', Area['Plo'](a, b, c))