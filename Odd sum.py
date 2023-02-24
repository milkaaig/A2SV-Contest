n = int(input())
two = list(map(int,input().split()))
flag = 0
two.sort()

if two.count(two[0]) == len(two):
    print(-1)
    flag = 1

if sum(two[:n]) != sum(two[n:]):
    if flag != 1:
        print(*two)
else:
    max1 = max(two[:n])
    
    min2 = min(two[n:])
    # print(max1, min2)
    i = two.index(max1)
    j = two.index(min2)
    
    two[i] = min2
    two[j] = max1
    if flag != 1:
        print(*two)

 
