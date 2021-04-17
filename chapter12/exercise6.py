def find_larg_word(words):
    unpacked = words
    for j in range(len(unpacked)):
        for i in range(len(unpacked)-1):
            if len(unpacked[i]) < len(unpacked[i+1]):
                a = unpacked[i]
                unpacked[i] = unpacked[i+1]
                unpacked[i+1] = a
    return unpacked  

def find_pce_by_pce(word):
    count = len(word) - 1
    a = []
    for i in range(len(word)):
        pce_word = word[0:count]
        a.append(pce_word)
        count = count - 1
    return a

def find_final_answer(words):
    a = find_larg_word(words)
    b = dict()
    for i in a:
        b[i] = find_pce_by_pce(i)
    return b

a = open("words1.txt")
b = []
for i in a:
    c = i.strip()
    b.append(c)

print(find_final_answer(b))

# print(find_pce_by_pce("ambuzz"))   
     
        

    