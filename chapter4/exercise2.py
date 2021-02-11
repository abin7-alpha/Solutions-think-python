from swampy.TurtleWorld import*
import math

def triangle(t, a, l):
    a = 360 / 3
    for i in range(3):    
        bk(t, l)
        rt(t, a)
    
def pentagon(t, n, a, l):
    
    for i in range(n):
        triangle(t, a, l)
        lt(t,360/n)
        
        
            
    
world = TurtleWorld()

bob = Turtle()

bob.delay = 0

#triangle(bob,30,50)
pentagon(bob,5,30,50)

die(bob)


wait_for_user()
