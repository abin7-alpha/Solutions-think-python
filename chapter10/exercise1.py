def nested_sum(t):
    total = 0
    for i in range(len(t)):
        a = sum(t[i])
        total = total + a
    return total    

t = [[1,3],[3,4],[5]]    
print(nested_sum(t))