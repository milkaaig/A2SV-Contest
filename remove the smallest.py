tc = int(input())

for i in  range(tc):
    
    size = int(input())
    a = list(map(int,input().split()))
    
    a = list(set(a))
    
    a.sort()
    
    size = len(a)
    
    output = 'YES'
    
    for j in range(size - 1):
        diff = a[j + 1] - a[j]
        
        if diff > 1:
            output = 'NO'
            break
        
    print(output)
        
