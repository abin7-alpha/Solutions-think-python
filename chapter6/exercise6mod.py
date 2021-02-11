def palindrome(word):
    
    if len(word) == 0:
        return True

    if word[0] != word[-1]:
        return False

    else:
        return palindrome(word[1:-1])


assert palindrome("mom") == True
assert palindrome("malayalam") == True
assert palindrome("kaka") == False
assert palindrome("m") == True
