
def fib(n):
    t1 = 0
    t2 = 1
    print(t1)
    print(t2)
    for i in range(n):
        a = t1 + t2
        t1 = t2
        t2 = a
        print(a)  


def fib(n):
    #basecase
    if n <= 1:
        return n

    # normal case
    else:
        return fib(n - 1) + fib(n - 2)


#print(fib(6))

#print([fib(n) for n in range(6)])

def fact(n):

    if n <= 1:
        return n
    else:
        return n * fact(n-1)
# print(fact(5))    

def power(n,p):
    if p == 1:
        return n
    else:
        return n * power(n,p-1)

#print(power(5,3))            


def check_fermat(a, b, c, n):
    if (n > 2) and pow(a, n) + pow(b, n) == pow(c, n):
        print('holy smokes')
    else:
        print('no, that doesn"t work')
