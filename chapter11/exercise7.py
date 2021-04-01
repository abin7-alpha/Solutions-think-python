def ack(m,n):
    a = {}
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        a[m, n] = ack(m-1,1)
        return a[m, n]
    elif m > 0 and n > 0:
        a[m, n] = ack(m-1,ack(m,n-1)) 
        return a[m, n]   

print(ack(4,4))
 