def reads(t):
    lists = []
    for i in t:
        lists.append(i)
    return lists

def reads2(t):
    a = []
    for i in t:
        a = a + [i]
    return a    

print(reads2(open("words.txt")))
# print(reads(open("words.txt")))