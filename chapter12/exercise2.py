import random

def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), random.random(), word)) 

    t.sort(reverse=True)

    res = []
    for length, a, word in t:
        res.append(word)
    return res

a = sort_by_length(["abin","jimbu","jiban","dani","ruban"])
for i in a:
    print(i)

