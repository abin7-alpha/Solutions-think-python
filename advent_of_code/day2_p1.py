valid = 0
valid2 = 0
for i in open("tests.txt"):
    seperate_part = i.split()
    print(seperate_part)
    seperate_firstpart = seperate_part[0].split("-")
    print(seperate_firstpart)
    maximum = int(seperate_firstpart[1])
    minimum = int(seperate_firstpart[0])
    password = seperate_part[2]
    seperate_secondpart = seperate_part[1].split(":")
    character = seperate_secondpart[0]
    
    count = 0
    for j in seperate_part[2]:
        if j == character:
            count = count+1
            print(count)

    # count = seperate_part[2].count(character)
    # print(count)


    
        if seperate_part[minimum-1] == character and seperate_part[maximum-1] != character:
            valid2 = valid2+1
        elif seperate_part[minimum-1] == character and seperate_part[maximum-1] == character:
            valid2 = valid2+1    


    if count >= minimum and count <= maximum:
        valid = valid+1
        print(valid)
    
     


print(f'no of valid  is {valid}')    
b = f'no of valis part2valid is {valid2}'
print(b)
