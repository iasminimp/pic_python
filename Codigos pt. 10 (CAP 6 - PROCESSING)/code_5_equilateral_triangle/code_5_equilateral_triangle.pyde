#Pagina 143
def setup(): #definição de tamanho da janela
    size(600,600)
    
def draw():
    translate(width/2, height/2)
    polygon(3,100) #3 = lados, 100 = unidades do vertice virada para o centro

def polygon(sides, sz): #desenha o poligono dado o numero de lados voltados para o centro    
    beginShape()
    for i in range(sides):
        step=radians(360/sides)
        vertex(sz*cos(i*step), 
              sz*sin(i*step))
    endShape(CLOSE)
    
