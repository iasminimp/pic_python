#exercise 1-6 a star is born
from turtle import *
shape ('turtle')

def starSpiral(lenght):
    for j in range (60):
        for i in range(5):
            forward(lenght)
            right(144) #180 - 36 = 144
        lenght+=5
        right(5)

starSpiral(1)
