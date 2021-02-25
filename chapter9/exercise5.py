def uses_all(word, string):
    for i in string:
        if i not in word:
            return False
    return True    

def avoid_words(word, string):
    count = 0
    for i in word:
        if uses_all(i, string) == True:
            count = count + 1
    return count        


print(avoid_words(open("words.txt"), "aeiou"))