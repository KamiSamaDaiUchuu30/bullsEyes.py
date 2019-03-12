from graphics import *

def circle(posX, posY, rad, color, bEwin):
    cir = Circle(Point(posX, posY), rad)
    cir.setFill(color_rgb(color, 0, 0))
    cir.draw(bEwin)
    
   
crSz = 50
color = 255
Win = GraphWin("bullesEyes", crSz*10 , crSz*10)
Win.setCoords(0, 0, crSz*10, crSz*10)

circle(150, 150, 50, color, Win)
