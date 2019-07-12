import turtle, random, time

# Звездное небо


def star_fill(n, weight):
    small_star.left(random.randint(10, 350))
    small_star.begin_fill()
    if n % 2 != 0:
        for _ in range(n):
            small_star.forward(weight)
            angle = n // 2 * 360 / n
            small_star.left(angle)
    small_star.end_fill()


desk = turtle.Screen()

desk.bgcolor("black")
desk.setup(900, 700)

small_star = turtle.Turtle()
small_star.speed(0)
small_star.color("yellow")
small_star.hideturtle()
for _ in range(19):
    x = random.randint(-320, 320)
    y = random.randint(-220, 220)
    small_star.up()
    small_star.setposition(x, y)
    small_star.down()
    size = random.randint(10, 20)
    ver = random.choice([5, 7, 9, 11, 13])
    star_fill(ver, size)


def move(a, b):
    small_star.up()
    small_star.setposition(a, b)
    small_star.down()
    squre = random.randint(10, 20)
    hight = random.choice([5, 7, 9, 11, 13])
    star_fill(hight, squre)


desk.onclick(move)
desk.listen()
desk.mainloop()
time.sleep(10)



