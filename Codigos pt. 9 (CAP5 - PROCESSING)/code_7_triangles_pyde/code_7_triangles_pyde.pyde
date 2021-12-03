#triangles.pyde
#pagina - 124

def setup():
    size(600,600)
    rectMode(CENTER)
t=0

def draw():
    global t
    translate(width/2, height/2)
    rotate(radians(t))
    triangle(0,0,100,100,200,-200)
    t+=0.5
    
