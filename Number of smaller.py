sizef , sizes = list(map(int,input().split()))
f = list(map(int,input().split()))
s = list(map(int,input().split()))
i = 0
count = 0
j = 0
output =[]
for i in range(sizes):
    if j == sizef:
        output.append(count)
    else:
        while j < sizef :
            if s[i] > f[j]:
                count += 1
                j += 1
            else:
                break
        output.append(count)
   
print(*output)
