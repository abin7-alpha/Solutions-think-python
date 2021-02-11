def find(word, letter, indexi):
    mod_word = word[indexi:]
    index = 0
    while index < len(mod_word):
        if mod_word[index] == letter:
            return index
        index = index + 1
    return -1

print(find("iam not okay", "k", 5))