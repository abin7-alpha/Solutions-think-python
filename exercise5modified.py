def printing_first():#prints the first line
    c = "+"+(" - "*4)
    d = c*4+" +"
    return d

def printing_second():#prints the second line
    b = "/            /            "*2
    a = b + " /"
    print(a)

def print_a():
    for i in range(4):#simple loop
        printing_second()
    print(printing_first())
    for j in range(4):#simple loop
        printing_second()
    print(printing_first())

def printing_all_in_order(a):
    print(printing_first())
    a()

    
def fourxfour(a):
    printing_all_in_order(a)
    a()

fourxfour(print_a)