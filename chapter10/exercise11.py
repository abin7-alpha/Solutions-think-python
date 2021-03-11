def reverse_pair(word):
    a = word[::-1]
    return a

def reverse_pair_list(word):
    reverse_list = []
    for i in word:
        reverse_list.append(reverse_pair(i.strip()))
    return reverse_list

def normal_list(word):
    lists = []
    for i in word:
        lists.append(i.strip())
    return lists

def in_bisecet(pac_list, a):
    mid = int(len(pac_list) / 2)
    if mid == 0:
        return False
    if pac_list[mid] == a:
        return True
    elif pac_list[mid] < a:
        b = pac_list[mid:len(pac_list)]
        return in_bisecet(b,a)
    else:
        c = pac_list[:mid]
        return in_bisecet(c,a)



reversed_list = reverse_pair_list(open("words.txt"))
norm_list = normal_list(open("words.txt"))
for word in reversed_list:
    if in_bisecet(norm_list, word) == True:
        print(word[::-1], word)

