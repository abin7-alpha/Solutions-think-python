list = [3,1,2,5,4,7,6]

def sort(list):

    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            a = list[i]
            list[i] = list[i+1]
            list[i+1] = a
        print(list)       

sort(list)