def key_method(dictionary):
    a = []
    for i in dictionary.keys():
        a.append(i)
    return a

def val_method(dictionary):
    a = []
    for i in dictionary.values():
        a.append(i)
    return a

def sorts(lists):
    a = sorted(lists) 
    return a   

dictionary = {'abin' : 7, 'jibin' : 4, 'cibin' : 5} 
a = key_method(dictionary)
b = val_method(dictionary)
print(sorts(a) , sorts(b))


