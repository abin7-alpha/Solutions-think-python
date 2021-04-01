def invert_dict(a):
    inverse_dict = dict()
    for i in a:
        val = a[i]
        if val not in inverse_dict:
            inverse_dict[val] = [i]
        else:
            inverse_dict[val].append(i)
    return inverse_dict

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0)+1
    return d        

a = histogram('parrot')
print(invert_dict(a))
