def count(word, letter):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    print(count)

count("malamyalam","a")