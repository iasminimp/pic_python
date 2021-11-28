#exercise 2-1: Somatorio de 1 até 100

#Somatorio de todos os numeros que o antecedem
def mySum(num):
    running_sum=0
    for i in range(1,num+1):
        running_sum+=i
    return running_sum

def cont(number): #função - contadora que chama a função
    #somatorio 100 vezes
    for i in range(number):
        print ('somatório (',i,') = ',mySum(i))

cont(101)#chamando a função cont para
#imprimir o somatorio dos números
