"""Reverse a string using recursion"""

def reverse_string(string,length,count):
    if length <= 0:
        return 
    else:
        print(string[count],end = "")
        reverse_string(string,length-1,count-1)      

a = "okaygoogle"
b = len(a)
count = -1
reverse_string(a,b,count)