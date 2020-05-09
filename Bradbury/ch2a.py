import turtle
#create window and turtle
window = turtle.Screen()
babbage = turtle.Turtle()

#draw stem and center
babbage.left(90)
babbage.forward(100)
babbage.right(90)
babbage.circle(10)

#draw all petals
for i in range (1,24):
    babbage.left(15)
    babbage.forward (50)
    babbage.left(157)
    babbage.forward (50)

#tidy up window


window.exitonclick()
