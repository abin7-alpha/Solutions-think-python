def calc_percentage(words):
    a = has_no_e(words) / 227617
    percentage = a * 100
    print(percentage)

def has_no_e(words):
    count = 0
    for word in words:
        if "e" not in word:
            count = count + 1
    return count   

calc_percentage(open("words.txt"))