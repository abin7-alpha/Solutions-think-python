def unpack(texts):
    dicts = dict()
    for i in texts:
        a = i.split(" ")
        key = a[0]
        value = a[1]
        dicts[key] = value.strip()
    return dicts

def word_freq(texts, word):
    dicts = dict()
    for i in word:
        if i in texts:
            dicts[i] = texts[i]
    return dicts        

def most_frequent(freq_dicts):
    a = []
    for i in freq_dicts:
        b = freq_dicts[i]
        a.append(float(b))
    return sorted(a)

def most_frequent2(lists):
    con_str_lis = []
    for i in lists:
        con_str_lis.append(str(i))
    return con_str_lis   

def most_frequent3(word,un_lists):
    for j in un_lists:
        if word == un_lists[j]:
            return j

unpacked_texts = unpack(open("char_freq.txt"))
freq_word = word_freq(unpacked_texts, "abin")
print(most_frequent2(most_frequent(freq_word)))
# for i in final_list:
#     print(most_frequent3(i, unpacked_texts))
