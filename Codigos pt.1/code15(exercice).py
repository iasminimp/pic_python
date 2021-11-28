c#exercise 1-5 - Turtle Espiral
from turtle import * #importação da biblioteca turtle
shape('turtle') #cursor no formato de tartaruga

def spiral (lenght): #função que ira fazer espiral
    for i in range (60): #laço que ira fazer o deslocamento do quadrado
    #laço que desenha o quadrado
        for j in range (4): 
            forward (lenght)
            right(90)
        right(5) #vira a direita no angulo de 5 graus
        lenght+=5 #é concatenado 5 ao tamanho dos lados do quadrado

spiral(1) #chamada da função Espiral
