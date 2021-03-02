def cumsum(t):
    a = []
    c = 0
    for i in range(len(t)):
        b = t[i] + c
        a.append(b)
        c = b
    return a    

t = [1,2,3,4,5]
print(cumsum(t))        

