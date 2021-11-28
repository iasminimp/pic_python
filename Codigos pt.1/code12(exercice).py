#exercise 1-4 Função Poligono

from turtle import * #importação da biblioteca turtle
shape('turtle') #cursor no formato de tartaruga

def polygon(sidelength): #função que faz o desenho
    for i in range(sidelength): #laço de repetição que se repete 4 vezes (lados do quadrado)
        right(60)#Ira vira a direita em sessenta graus
        forward(100)
        
        
polygon(10)#chamando a função QUADRADO e passando, parametro, como valor 30

