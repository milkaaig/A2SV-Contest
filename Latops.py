from collections import defaultdict
lapn = int(input())
lap = defaultdict(list)
for i in range(lapn):
    lap[i] = list(map(int,input().split()))
flag = 0
count = 0
for i in range(len(lap)):
    if lap[i][0] < lap[i][1]:
        for  j in range(len(lap)):
            if lap[j][0] > lap[i][0] and lap[j][1] < lap[i][1]:
                print("Happy Alex")
                count = 0
                flag = 1
                break
        
        if flag == 1:
            break
    count += 1
if count != 0 and flag != 1:
    print("Poor Alex")
    
            
