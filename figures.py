from turtle import *
def star(c,side,colr,fill=False):
    pencolor(colr)
    i=Turtle()
    u=360/c

    if fill:
        i.begin_fill()

    
    for o in range(c):
        i.forward(side)
        i.right(u*2)
        i.forward(side)
        i.left(u)

    if fill:
        i.end_fill()
star(30,50,"black",fill=True)