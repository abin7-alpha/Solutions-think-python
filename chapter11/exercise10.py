def rotate_letter(letter, number):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    location = find_location(letter, alphabets)
    if location + number > 25:
        return alphabets[location + number - 26]         
    return alphabets[location+number]

def find_location(character, string):
    location = 0
    for i in string:
        if i == character:
            break
        location += 1
    return location    

def rotate_word(word, number):
    final_word = ""
    for i in word:
        j = rotate_letter(i, number)
        final_word = final_word + j
    return final_word   

def make_word_dict():
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d     

def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in word_dict:
            print (word, i, rotated)

words = make_word_dict()
for word in words:
    rotate_pairs(word, words)

     
