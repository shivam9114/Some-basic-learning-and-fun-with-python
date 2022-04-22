import turtle

def drawRectangle (t, w, h, c):
    t.fillcolor(c)
    t.begin_fill()
    for i in range(2):
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
    t.end_fill()


def main ():
    wn = turtle.Screen()

    chloe = turtle.Turtle()
    drawRectangle(chloe,50,200, "orange1")

    chloe.up()
    chloe.goto(0,-100)
    chloe.down()

    drawRectangle(chloe,50,200, "chartreuse3")

    chloe.up()
    chloe.goto(100,-25)
    chloe.down()
    chloe.pencolor("blue4")

    for i in range(24):
        chloe.forward(20)
        chloe.backward(20)
        chloe.left(15)
    chloe.up()
    chloe.goto(300,300)

main()
#to hold the
#output window
turtle.done()
