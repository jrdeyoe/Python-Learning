import turtle

def drawTri(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0], points[1][1])
    myTurtle.goto(points[2][0], points[2][1])
    myTurtle.goto(points[0][0], points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def sierp(points,degree,myTurtle):
    colormap = ["black","white","white","white","white","white"]
    drawTri(points,colormap[degree],myTurtle)
    if degree > 0:
        sierp([points[0],getMid(points[0], points[1]),getMid(points[0], points[2])],degree-1, myTurtle)
        sierp([points[1],getMid(points[0], points[1]),getMid(points[1], points[2])],degree-1, myTurtle)
        sierp([points[2],getMid(points[2], points[1]),getMid(points[0], points[2])],degree-1, myTurtle)

def main():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myPoints = [[-300,-250],[0,100],[300,-250]]
    sierp(myPoints,5,myTurtle)
    myWin.exitonclick()

main()