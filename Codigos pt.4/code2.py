#função que calcula o x
#x = ( d - b )
#    ---------
#    ( a - c )


def equation(a,b,c,d):
    #resolve a equação de forma: ax + b = cx+d
    return (d-b)/(a-c)

#exemplos
print (equation (2,5,0,13)) #4.0

print (equation (12,18,-34,67)) #1.06521
