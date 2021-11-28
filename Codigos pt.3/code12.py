from random import randint#Usando um loop para advinhação/ tente novamente
def numberGame():
    #escolhe um numero aleatorio(entre 1 e 100)
    number= randint(1,100)
    print("Eu estou pensando em um número entre 1 e 100.")
    palpite = int(input("Qual o seu palpite?"))

    while palpite:
        if (number == palpite):
            print("Isso mesmo, parabéns seu palpite esta correto!")
            break
        elif (number>palpite):
            print("Não foi dessa vez... dica, o número é maior")
        else:
            print("Não foi dessa vez,... dica: o número é menor")
        palpite = int(input("Qual o seu palpiteh?"))

numberGame()
