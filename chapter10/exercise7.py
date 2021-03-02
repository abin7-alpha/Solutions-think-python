def has_duplicates(t):
    for i in range(len(t)):
        a = t[i+1 : len(t)]
        if t[i] in a:
            return True
    return False 

t = ["c","b","d","c"]
print(has_duplicates(t))                         