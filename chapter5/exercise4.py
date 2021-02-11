def is_traingle(a,c,d):
    h = a+c
    i = a+d
    j = c+d
    if d > h:
        print("triangle cannot be formed")
    elif c > i:
        print("triangle cannot be formed")    
    elif a > j:
        print("traingle cannot be formed")
    else:
        print("triangle can be formed")

is_traingle(6,4,6)                