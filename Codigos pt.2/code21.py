#Função Mysum

#Somatorio de todos os numeros que o antecedem
def mySum(num):
    running_sum=0
    for i in range(1,num+1):
        running_sum+=i
    return running_sum

print(mySum(10)) #55

print(mySum(100)) #5050
