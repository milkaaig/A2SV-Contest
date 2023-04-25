tc = int(input())
for i in range(tc):

    nfav, x = (map(int, input().split()))
    fav =  list(map(int, input().split()))
    sumof = (x * (x + 1)) // 2

    for i in fav:
        if i <= x:
            sumof -= i * 2
    
    print(sumof)

