import random
"""to find the random birth date"""
def random_birth_date():
    aa = (random.randint(1,31))
    return aa

"""to find the random bithdate of 23 students"""
def all_birthdate(n):
    a = []
    for i in range(n):
        a = a + [random_birth_date()]
    print(a)     
    return a

"""to find the duplicate birth dates"""
def has_duplicates2(n):
    a = []
    for i in n:
        if i not in a:
            a.append(i)
    return a        

"""to calculate the count of duplicates"""
def has_duplicates(a,b):
    no_duplicates = []
    for i in b:
        c = a.count(i)
        if c > 1:
            no_duplicates.append(c)
    return no_duplicates      

"""to fid the dates with more than 1 duplicates"""
def has_duplicates3(a,b):
    dates = []
    for i in b:
        c = a.count(i)
        if c > 1:
            dates.append(i)
    return dates     
   

a = all_birthdate(23)
b = has_duplicates2(a)  
c = has_duplicates(a,b)
d = has_duplicates3(a,b)
count1 = 0
for i in range(len(has_duplicates(a,b))):
    print(f'{c[count1]} students with date of {d[count1]} ')
    count1 += 1

