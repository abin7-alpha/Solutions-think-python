def find_locaton(first_letter):
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    count = 0
    for i in alphabets:
        if i == first_letter:
            break
        count = count + 1       
    return count    

def is_true(word):
    count1 = 0
    for i in range(len(word)-1):
        if find_locaton(word[count1]) > find_locaton(word[count1 + 1]):
            return False
        count1 = count1 + 1   
    return True


def is_abcedarian(word):
    count = 0
    for i in word:
        if is_true(i) == True:
            count = count + 1
    return count        

    
                
# print(is_true("abcf"))
print(is_abcedarian(open("words.txt")))       