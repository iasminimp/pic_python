from turtle import * #importação da biblioteca turtle
shape('turtle') #cursor no formato de tartaruga

def square(sidelength): #função que faz o desenho do quadrado (recebe um parametro)
    for i in range(4): #laço de repetição que se repete 4 vezes (lados do quadrado)
        forward(sidelength) #ira avançar, no desenho, o tamanho de SIDELENGTH
        right(90)#Em seguida ira vira a direita em noventa graus
square(30)
square(50)       
square(100)#chamando a função QUADRADO e passando, parametro, como valor 100

#logo, nesse caso
#sidelength = 100
