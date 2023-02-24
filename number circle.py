non = int(input())
num = list(map(int,input().split()))
num.sort()
lastel = non - 1
if num[lastel] < num[lastel - 1] + num[lastel - 2]:
    temp = num[lastel - 1]
    num[lastel-1] = num[lastel]
    num[lastel] = temp
    print("YES")
    for i in num:
        print(i, end=" ")
else:
    print("NO")
