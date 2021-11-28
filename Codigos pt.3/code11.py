from random import randint #importação da biblioteca randint/random

def numberGame():   
    number = randint(1,100)#escolher um numero aleatorio entre 1 e 100    
    #exibe para o usuário
    print("Eu estou pensando em um número entre 1 e 100.")
    palpite = int(input("Qual o seu palpite? "))
    #condicionais, que comparam o numero escolhido aleatoriamente e o que palpite
    if (number==palpite):
        print("É isso mesmo, esse é o número \0/")
    elif(number>palpite):
        print("Poxa...:/. É um pouco maior")
    else:
        print("Poxa, é um pouco menor  :/")
    #print(number)
numberGame() #chamada da função

    
