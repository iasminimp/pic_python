def setup(): #tamanho da janela
    size(400,400)
    
def draw():
    #width e height -> definido pela função setup/ draw .. no caso 400
    translate(width/2,height/2); #reposiciona o quadrado/ desenho
    #translate(right,down)
    rect(50,100,100,60)
    #rect(x,y,width, height)
    #x e y => cordenadas
    #width e height -> altura e largura
