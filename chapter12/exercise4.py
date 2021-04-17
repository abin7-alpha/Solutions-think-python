def unpack(words):
    a = []
    for i in words:
        b = i.strip()
        a.append(b)
    return a

def anagram(word1,word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False    

def anagram2(unpacked):    
    d = {}
    for i in unpacked:
        for j in unpacked:
            if anagram(i, j):
                if i not in d:
                    d[i] = [j]
                else:
                    d[i].append(j)
    return d    

def ques_2(unpacked):
    a = []
    for v in unpacked.values():
        a.append(v)
    return a    

def ques_2_2(final_list):
    unpacked = final_list
    for j in range(len(unpacked)):
        for i in range(len(unpacked)-1):
            if len(unpacked[i]) < len(unpacked[i+1]):
                a = unpacked[i]
                unpacked[i] = unpacked[i+1]
                unpacked[i+1] = a
    return unpacked    

def ques_3(unpacked):
    a = []
    for i in unpacked.values():
        if len(i) == 8:
            a.append(i)
    return a                    

unpacked = unpack(open("words1.txt"))
# print(anagram2(unpacked))
b = ques_2(anagram2(unpacked))
print(ques_2_2(b))