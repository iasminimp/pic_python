#circleSine Wave #pagina 41-part2
r1 = 100 #raio do maior circulo
r2 = 10 #raio do menor circulo
t=0 #tempo da variavel

def setup(): #define o tamanho da janela 
    size(600,600)

def draw():
    global t
    background(200)
    #move para centro esquerdo da tela
    translate(width/4,height/2)
    noFill() #circulo transparente
    stroke(0)#linha na cor preta
    ellipse(0,0,2*r1,2*r1)
    
    #circulo/ ellipse
    fill(255,0,0) #cor: vermelha
    y = r1*sin(t)
    x=r1*cos(t)
    ellipse(x,y,r2,r2)
    t+=0.05
