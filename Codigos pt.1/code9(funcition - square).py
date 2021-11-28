from turtle import * #importação da biblioteca turtle
shape('turtle') #cursor em formato de tartaruga

def square(): #função Quadrado, sem parametros
    for i in range(4): #loop que irá se repetir 4 vezes
        forward(100) #irá avançar 100 passos
        right(90)# em seguida irá virar em 90 graus

square() #chamando a função quadrado
