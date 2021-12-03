#pagina - 134

def setup():
    size(600,600)
    rectMode(CENTER)
    
t=0

def draw():
    global t
    background(255) #fundo branco
    translate(width/2, height/2)
    for i in range(90):
        rotate(radians(360/90)) #space the triangles evenly
        pushMatrix() #salva a orientação da rotação
        translate(200,0) #go to circumference of circle
        rotate(radians(t+2*i*360/90))#spin each triangle
        tri(100) #desenha o triangulo
        popMatrix() #retorna para salvar a orientação
    t+=0.5
    
def tri(length): #desenha um triangulo equilatero no centro (0,0)
    noFill() #deixa o triangulo transparente
    triangle(0,-length,-length*sqrt(3)/2, length/2,length*sqrt(3)/2, length/2)
    
    
