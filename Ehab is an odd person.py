n = int(input())
array = list(map(int,input().split()))

even = False 
odd = False 

for i in range(n):
    
    if array[i] % 2 == 0:
        even = True 
    else :
        odd = True 
    i += 1 

if even and odd:
    array.sort()
print(*array)
