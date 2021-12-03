#colorGrid.pyde - pagina 121

def setup ():
    size(600,600)
    
def draw ():
    background(255) #cor do fundo - branca
    for x in range(20):
        for y in range(20):
            rect(30*x,30*y,25,25)
