import turtle
desk = turtle.Screen()
r = 100

europe = turtle.Turtle()
africa = turtle.Turtle()
usa = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()

for i in [europe, africa, usa, asia, australia]:
    i.up()

europe.goto(-2 * r,  2 * r)
africa.goto(0, 2 * r)
usa.goto(2 * r, 2 * r)
asia.goto(-r, r)
australia.goto(r, r)

for i in [europe, africa, usa, asia, australia]:
    i.down()
    i.pensize(4)

europe.color("blue")
africa.color("black")
usa.color("red")
asia.color("yellow")
australia.color("green")

for i in [europe, africa, usa, asia, australia]:
    i.circle(r)

desk.mainloop()
