#exercise 1-3

from turtle import * #importação da biblioteca turtle
shape('turtle') #cursor no formato de tartaruga

def triangle(sidelength): #função que faz o desenho do quadrado (recebe um parametro)
    for i in range(3): #laço de repetição que se repete 4 vezes (lados do quadrado)
        right(60)#Ira vira a direita em sessenta graus
        forward(sidelength) #ira avançar, no desenho, o tamanho de SIDELENGTH
        right(60)#Em seguida ira vira a direita em sessenta graus

triangle(30)#chamando a função QUADRADO e passando, parametro, como valor 30
triangle(50)#chamando a função QUADRADO e passando, parametro, como valor 50      
triangle(100)#chamando a função QUADRADO e passando, parametro, como valor 100



