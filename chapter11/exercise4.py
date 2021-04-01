def mod_reverse_lookup(a, v, d): 
    c = []
    b = []
    if reverse_lookup(v,d) != True:
        return b
    c.append(a)
    return c    

def reverse_lookup(v,d):
    for i in d:
        if d[i] == v:
            return True
    return False

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d    

a = 'parrot'
h = histogram(a)
print(mod_reverse_lookup(a, 3, h))      