def interlock1(word):
    a = word[::2]
    return a

def interock2(word):
    b = word[1::2]
    return b

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

pac_list = normal_list(open("words.txt"))
for i in pac_list:
    if in_bisecet(pac_list, interlock1(i)) and in_bisecet(pac_list, interock2(i)):
        print(i,interlock1(i),interock2(i))