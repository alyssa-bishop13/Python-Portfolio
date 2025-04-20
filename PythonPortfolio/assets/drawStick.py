import turtle

t = turtle.Turtle()
t.color("hotpink")
t.pensize(4)
t.speed(3)
#head circle
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(20)
#line down - body
t.right(90)
t.forward(60)
#arms / legs - down
t.backward(40)
t.left(45)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(40)
t.backward(40)
t.left(45)
t.forward(40)
t.left(30)
t.forward(40)
t.backward(40)
t.right(60)
t.forward(40)

t.hideturtle()
turtle.done()