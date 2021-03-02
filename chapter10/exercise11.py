"""to check whether the word is reverse order"""
def reverse_pair(t):
    count = 0
    count2 = -1
    if len(t) <= 2:
        return True
    for i in range(len(t)):
        if t[count] != t[count2]:
            return False
        count += 1
        count2 += -1
    return True        

"""to unpack the txt file"""
def unpack_words():
    rev_pair = 0
    for i in open("words.txt"):
        if reverse_pair(i) == True:
            rev_pair = rev_pair + 1
    return rev_pair                    

print(unpack_words())
# print(reverse_pair("a"))
