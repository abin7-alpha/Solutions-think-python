for i in open("words.txt"):
    word = i.strip()
    if len(word) > 20:
        print(word)