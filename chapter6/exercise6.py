def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
    
def full_word(h):
    print(first(h))
    print(last(h))
    print(middle(h))

def is_palindrome(word):
    
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))    


a = 0
wor = "mom"
lengt = len(wor)
print(is_palindrome(wor))