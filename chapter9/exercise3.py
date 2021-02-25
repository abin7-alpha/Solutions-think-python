def avoid(word, string):
    for i in word:
        for j in string:
            if i == j:
                return False
    return True 

def avoid_words(word, string):
    count = 0
    for i in word:
        if avoid(i, string) == True:
            count = count + 1
    return count           
          
string = input("enter 5 forbidden letters:").strip()
if len(string) > 5:
    print("only 5 letters forbides")
else:
    print(avoid_words(open("words.txt"), string))