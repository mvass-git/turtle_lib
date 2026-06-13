import turtle

def poly(side,lenght,color,fill=False):
    a=((side-2)*180)/side
    tu =turtle.Turtle()
    s=turtle.Screen()
    tu.color(color)
    if fill:
        tu.begin_fill()
    for i in range(side):
        tu.forward(lenght)
        tu.right(a)
    if fill:
        tu.end_fill()

    s.exitonclick()
    