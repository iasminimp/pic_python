#Pagina 142
def setup(): #definição de tamanho da janela
    size(600,600)
    
def draw():
    translate(width/2, height/2)
    beginShape()
    for i in range(6):
        vertex(100*cos(radians(60*i)), 100*sin(radians(60*i)))
    endShape(CLOSE)
    
