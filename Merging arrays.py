lf , ls = list(map(int, input().split()))
first = list(map(int, input().split()))
sec = list(map(int, input().split()))
output = []

for i in first:
    output.append(i)

for i in sec:
    output.append(i)
    
output.sort()

    
   

print(*output)
        
