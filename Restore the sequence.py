tc = int(input())

for i in range(tc):
    ls = int(input())
    s = list(map(int, input().split()))
    output = []
    l = 0
    r = ls-1
    
    if ls == 1:
        output.append(s[0])
    else:
    
        for i in range(ls):
            output.append(s[l])
            output.append(s[r])
            l += 1
            r -= 1
            
            if l > r:
                break
            if l == r:
                output.append(s[l])
                break
        
    print(*output)
