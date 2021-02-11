def multilication_table(n,a):
    if n <= 0:
        return False
    else:
        multilication_table(n-1,a)
        print(n*a)

multilication_table(10,2)        