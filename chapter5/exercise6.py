from swampy.TurtleWorld import*

def koch(t, n):
    """Draws a koch curve with length n."""
    if n<3:
        fd(t, n)
        return
    m = n/3.0
    koch(t, m)
    lt(t, 60)
    koch(t, m)
    rt(t, 120)
    koch(t, m)
    lt(t, 60)
    koch(t, m)

world = TurtleWorld()

bob = Turtle()



bob.set_color("yellow")
bob.set_pen_color("red")
bob.delay = 0.01
koch(bob,60)    

call_user()    