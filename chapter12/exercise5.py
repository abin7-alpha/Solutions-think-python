def metathesis(word1, word2):
    if len(word1) != len(word2):
        return False
    a = zip(word1,word2)    
    if sorted(word1) == sorted(word2):   
        count = 0
        if word1 == word2:
            return False
        for i,j in a:
            if i != j:
                count = count + 1
        if count == 2:
            return True
        if count > 2:
            return False  
    else:
        return False          


# print(metathesis("ab", "ba"))    
b = dict()
a = open("words1.txt")
for i in a:
    for j in a:
        if metathesis(i, j):
            if i not in b:
                b[i] = j
            else:
                b[i].append(j)

print(b)
               