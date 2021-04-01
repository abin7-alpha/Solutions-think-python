def fibonacci(n, known):
    if n in known:
        return known[n]

    res = fibonacci(n-1,known) + fibonacci(n-2,known)
    
    known[n] = res
    return res

known = {0:0, 1:1}
print(fibonacci(5, known))