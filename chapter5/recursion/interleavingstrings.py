"""Find all interleavings of given strings"""

def interleaving(str1,str2,length):
    string = str1+str2
    length = len(string)
    print(string)
    print(length)
    a = string[i+1]
    string[i+1] = string[i]
    string[i] = a
    string

    
interleaving("ab","da")

    
    
