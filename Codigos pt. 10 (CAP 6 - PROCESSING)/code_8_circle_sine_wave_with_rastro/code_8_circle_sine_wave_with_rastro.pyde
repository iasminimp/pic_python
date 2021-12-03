#circleSine Wave #pagina 42-part2
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
    circleList = []
    global t, circleList
    #circleList.insert(0,y)

    
    ellipse(x,y,r2,r2)
    stroke(0,255,0)#verde para linha
    line(x,y,200,y)
    fill(0,255,0)#verde para ellipse
    ellipse(200,y,10,10)
    #loop over cicleList para deixar um rastro
    for i in range(len(circleList)):
        ellipse(200+i,circleList[i],5,5)
    
    t+=.05
    
