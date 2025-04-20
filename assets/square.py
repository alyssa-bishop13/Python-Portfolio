import turtle
t = turtle.Turtle()
x = int(input("Enter a number: "))
def draw_square():
    for i in range(4):
        t.forward(x)
        t.right(90)

print(draw_square())

turtle.done()