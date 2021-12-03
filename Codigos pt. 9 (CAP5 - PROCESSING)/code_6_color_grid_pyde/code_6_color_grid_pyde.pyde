#colorGrid.pyde - pagina 122
#d = dist(30*x,30*y, mouseX, mouseY)
def setup ():
    size(600,600)
    rectMode(CENTER)
   colorMode(HSB) #1
    
def draw ():
    background(0) #cor do fundo - preto
    translate(20,20)
    for x in range(30):
        for y in range(30):
            d = dist(30*x,30*y, mouseX, mouseY)
            fill(0.5*d,255,255)
            rect(30*x,30*y,25,25)
