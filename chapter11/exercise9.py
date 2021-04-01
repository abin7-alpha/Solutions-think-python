def convert_dict2(a, b):
    b.pop(a)
    return b

def convert_dict1(words):
    a = {}
    for i in words:
        a[i] = 0
    return a

def has_duplicates(word, words):
        if word in words:
            return True
        else:
            return False    

for_convert2 = convert_dict1(open('words.txt'))
count = 0
for i in for_convert2:
    a = convert_dict2(i, for_convert2)
    if has_duplicates(i, a) == True:
        count = count + 1

print(count)    



    
    