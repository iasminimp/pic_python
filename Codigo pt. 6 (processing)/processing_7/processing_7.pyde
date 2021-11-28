#grid.pyde
xmin=-10 #set the range of x-values
xmax=10
#range of y-values
ymin=-10
ymax=10
#calculate the range
rangex= xmax-xmin
rangey = ymax - ymin
def setup():
    global xscl, yscl
    size(600,600)
    xscl = width/rangex
    yscl = -height/ rangey    
#desenhando a grade
def draw():
    global xscl, yscl
    background (255) #fundo branco
    translate(width/2, height/2)
    grid(xscl, yscl)
    graphFunction()
    
def f(x): #função
    return x**2

def graphFunction():
    x=xmin
    while x<= xmax:
        fill(0)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x+=0.1
        
#desenha uma grade para o grafico
def grid (xscl, yscl):
    strokeWeight(1)#cyan lines
    stroke(0,255,255)
    for i in range(xmin,xmax+1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) #black axes
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)

        
