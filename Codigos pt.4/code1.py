#chapter 4
def plug(): 
    x=-100 #x começa valendo -100
    while(x<100): #enquanto x menor que 100
        if (2*x+5)==13: #se essa/ quando a equação for verdadeira
            print("x = ",x) #imprime o x que satisfaz a equação
        x+=1#caso ainda não for satisfeita a equação, ira iterar 1, no valor de x
plug() #chamando a função
