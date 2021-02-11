from swampy.TurtleWorld import*

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

world = TurtleWorld()

bob = Turtle()



bob.set_color("yellow")
bob.set_pen_color("red")
bob.delay = 0.01
draw(bob,5,9)    

call_user()