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

        

print(rotate_word('xyz', 3))#== 'def'
#print(rotate_letter("c",3))
# find_location("a","car")