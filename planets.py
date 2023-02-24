from collections import Counter

testcases = int(input())

for i in range(testcases):
    numplancost = input().split()
    cost = int(numplancost[1])
   
    
    mincost = 0
    orbits = Counter(input().split())
    for i in orbits.values():
       if i >= cost:
           mincost += cost
       else:
           mincost += i
    print(mincost)
            
    
            
