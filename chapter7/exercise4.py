import math

def eval_loop():
    
    while True:
        a = input("input:")
        b = eval(a)
        if b == "done":
            break
        print(b)
    return b



eval_loop()            
