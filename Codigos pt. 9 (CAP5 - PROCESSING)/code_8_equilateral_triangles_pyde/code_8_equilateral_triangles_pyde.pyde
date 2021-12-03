#rotation_triangle.pyde
#pagina - 129

def setup():
    size(600,600)
    rectMode(CENTER)
t=0

def draw():
    global t
    translate(width/2, height/2)
    rotate(radians(t))
    tri(200)
    t+=0.5
    
def tri(length): #desenha um triangulo equilatero no centro (0,0)
    triangle(0,-length,-length*sqrt(3)/2, length/2,length*sqrt(3)/2, length/2)
    
    
