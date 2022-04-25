import os
import math

clear = lambda: os.system('cls')
result = 0

def Line(s):
    clear()
    print("line - " + str(s))
    print("length = " + str(len(s)))
    print("Number of spaces = " + str(s.count(' ')))
    print("Number of commas = " + str(s.count(',')))