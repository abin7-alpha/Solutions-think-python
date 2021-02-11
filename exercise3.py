def right_justify(s):
    c = len(s)
    d = 70 - c
    f = d*" "+s
    return f

c = input("enter the word:")  
print(right_justify(c))


# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()   

# def print_lyrics():
#     print ("I'm a lumberjack, and I'm okay.")
#     print ("I sleep all night and I work all day.")

# repeat_lyrics()    