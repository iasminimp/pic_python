#somatorio de listas
print(sum([8,11,15])) #34

#tamanho de listas
print(len([8,11,15])) #3

#Com as duas funções (Len e Sum) podemos fazer
#a media de listas, com a seguinte função
def average3(numList):
    return sum(numList)/len(numList)

media = average3([8,11,15])
print(media) #11.3333
