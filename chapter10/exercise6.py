def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False
    for i in word1:
        if i not in word2:
            return False
    return True        

print(is_anagram("mom","mmo"))