#definição do formato de funções matemáticas
import math #importação da biblioteca de matemática


#x é um numero passado coo parametro
def f(x): #função que recebe um parametro
    return math.sqrt(x+3)-x+1 #e retorna a raiz quadradada do numero +3 - numero +1


#laço de repetição for que exibe a lista dos valores para o usuário
for x in[0,1,math.sqrt(2)-1]:
    print("f({:.3f}) = {:.3f}".format(x,f(x)))
    
