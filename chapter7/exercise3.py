import math

def count(n):
        return float(n)
    
def mathsqrt(n):
        return math.sqrt(n)

def newtons_method(n):
    x = n/2
    while True:
        y = (x + n/x) / 2
        if y == x:
            return x
            break
        x = y    
def differnce(n):
    return newtons_method(n) - mathsqrt(n)

def test_square(a):
    for a in range(1,a+1):
        # print(count(a),newtons_method(a),mathsqrt(a),differnce(a))
        # print(f"{count(a)} {newtons_method(a)} {mathsqrt(a)} {differnce(a)}")
        print(count(a), "{:<9f}".format(newtons_method(a)), "{:<9f}".format(mathsqrt(a)), differnce(a))


# mathsqrt(9)
# section7_5(9)
# print(newtons_method(1))
test_square(9)
