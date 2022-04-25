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

def Line(s):
    clear()
    print("line - " + str(s))
    print("length = " + str(len(s)))
    print("Number of spaces = " + str(s.count(' ')))
    print("Number of commas = " + str(s.count(',')))



while True:
    print("Choose the right option:"
          "\n 1. Calculator"
          "\n 2. Counting in line"
          "\n 3. Мatrix"
          "\n 0. Cancel")
    try:
        variant = int(input())
        if (variant == 1):
            while True:
                clear()
                print("Choose the right option:"
                      "\n 1. Calculator"
                      "\n 0. Cancel")
                calculate = int(input())
                if (calculate == 0):
                    clear()
                    break
                if (calculate == 1):
                    print("Enter numbers: \n")
                    a = float(input())
                    b = float(input())
                    while True:
                        print("\n Choose the right option:"
                              "\n 1. Addition"
                              "\n 2. Subtraction"
                              "\n 3. Multiplication"
                              "\n 4. Division"
                              "\n 5. Division by integer"
                              "\n 6. Root"
                              "\n 7. Finding the remainder"
                              "\n 8. Area and perimeter of a parallelepiped"
                              "\n 0. Cancel")
                        number = int(input())
                        Calculate(a, b, number)
                        if (number == 0):
                            clear()
                            break
        elif (variant == 0):
            print("Good luck")
            break
        elif (variant == 2):
            print("Complete the line: ")
            s = str(input())
            if(s != ""):
                Line(s)
        elif (variant == 3):
            print("Enter the number of columns: ")
            N = int(input())
            print("Enter the number of lines: ")
            M = int(input())
            A = []
            for i in range(N):
                A.append([0] * M)
            print("Enter the first number: ")
            g = int(input())
            print("Increase: ")
            c = int(input())
            for i in range(N):
                for j in range(M):
                    A[i][j] = g
                    g += c

            for i in range(len(A)):
                for j in range(len(A[i])):
                    print(A[i][j], end=' ')
                print()
            print("The matrix has " + str(N) + " columns and " + str(M) + " string(-s) \n" )
    except:
        clear()
        print("Data entered incorrectly!!!")