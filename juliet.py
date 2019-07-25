import turtle, time

juliet = turtle.Turtle()
romeo = turtle.Turtle()

juliet.color("misty rose")
juliet.width(3)

romeo.color("violet")
romeo.width(3)


romeo_last_name = "montaque"

romeo.left(40)
romeo.forward(100)

for side in range(185):
    romeo.forward(1)
    romeo.left(1)
romeo.hideturtle()

if romeo_last_name == "montaque":
    juliet.left(140)
    juliet.forward(100)
    for side in range(185):
        juliet.forward(1)
        juliet.right(1)
    juliet.hideturtle()

time.sleep(10)