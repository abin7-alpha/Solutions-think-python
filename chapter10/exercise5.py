def is_sorted(t):
    if t == sorted(t):
        return True
    else:
        return False    

t = ["a","c","b"]
print(is_sorted(t))            