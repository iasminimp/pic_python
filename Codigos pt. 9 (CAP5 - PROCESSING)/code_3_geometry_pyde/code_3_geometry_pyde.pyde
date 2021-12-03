#geometry.pyde
t=0
def setup():
    size(600,600)

def draw():
    global t
    background(255) #setar o fundo de cor branco
    translate(width/2, height/2)
    rotate(radians(t))
    
    for i in range(12):
        pushMatrix()#salva a orientação
        translate(200,0)
        rotate(radians(t))
        rect(0,0,50,50)
        popMatrix()#retorna para a orientação salva
        rotate(radians (360/12))
    t+=1
