from swampy.TurtleWorld import*
import math


#length = int(input("what is the length of the square that turtle need to draw:"))
#def wait_for_the_user():
    #for i in range(4):
    	#bk(bob, length)
    	#rt(bob)
    
    
def square(t, length):
    for i in range(8):
        bk(t, length)
        rt(t)
        
def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        bk(t, length)
        rt(t, angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 100
    length = circumference / n
    polygon(t, n, length)
                
def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    
    for i in range(n):
        fd(t, step_length)
        lt(t, step_angle)

def petal(t, r, angle):
    
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180-angle) 
        
def flower(t, n, r, angle):


    for i in range(n):
        petal(t, r, angle)
        lt(t, 360/n)           
            
def move(t , length):
    pu(t)
    fd(t, length)
    pd(t)
    
    

        
world = TurtleWorld()

bob = Turtle()



bob.set_color("yellow")
bob.set_pen_color("red")
bob.delay = 0.01

#square(bob, 50)
#polygon(bob,4,45)
#circle(bob,50)
#arc(bob,100,45)
#petal(bob,100,45)
#flower(bob,6,100,45)
move(bob, -100)
flower(bob, 7, 60.0, 60.0)

move(bob, 100)
flower(bob, 10, 40.0, 80.0)

move(bob, 100)
flower(bob, 20, 140.0, 20.0)

die(bob)
from swampy.TurtleWorld import TurtleWorld, Turtle
#create the World
world = TurtleWorld(interactive=True)
# create the Turtle
turtle = Turtle()
# wait for the user
world.mainloop()
