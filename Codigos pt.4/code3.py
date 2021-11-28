from math import sqrt #importação da biblioteca de matematica

def quad (a,b,c):
    #retorna a solução da equação a*x**2 + b-x + c =0
    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2= (-b - sqrt(b**2-4*a*c))/(2*a)
    return x1,x2

print(quad(2,7,-15)) #(1.5,-5.0)
