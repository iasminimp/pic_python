#Função Mysum2
#Somatorio de (n^2) + 1
def mySum2(num):
    running_sum=0
    for i in range(num+1):
        running_sum+=i**2+1
    return running_sum
print(mySum2(10)) #396
print(mySum2(20)) #2891
print(mySum2(100)) #338451
