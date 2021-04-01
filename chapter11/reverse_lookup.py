def reverse_lookup(v,d):
    for i in d:
        if d[i] == v:
            return i
    raise ValueError

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d    

h = histogram('parrot')
print(reverse_lookup(2, h))      