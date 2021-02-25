def uses_all(word, string):
    for i in string:
        for j in word:
            if i != j:
                return False
    return True            

print(uses_all("imeiou","abcdef"))