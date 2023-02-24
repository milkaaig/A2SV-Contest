size = int(input())
a = list(map(int, input().split()))

l = 0
r = size - 1
while l < size - 1:
    if a[l] > a[l+1]:
        break
    l += 1
    
while r > l:
    if a[r] < a[r - 1]:
        break
    r -= 1
    
if r < size - 1 and a[l] > a[r + 1] or l > 0 and a[r] < a[l -1]:
    print("no")
    quit()

for i in range(l, r):
    if a[i] < a[i + 1]:
        print("no")
        quit()
        
print("yes")
print(l + 1, r + 1)
    




        
       
