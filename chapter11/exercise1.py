def pack_dict(words):
    n = 0
    word = {}
    for i in words:
        word[i] = n
        n = n + 1
    return word

def search(n_word, a):
    if n_word in a:
        return True

a = (pack_dict(open("words.txt")))
print(search("yows\n", a))



