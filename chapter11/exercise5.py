def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d    

def mod_invert_dict(a):
    inverse = dict()
    for i in a:
        inverse.setdefault(a[i],[]).append(i)
    return inverse

a = histogram('parrot')
print(mod_invert_dict(a))



