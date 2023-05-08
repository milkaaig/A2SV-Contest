import heapq

tc = int(input())

for i in range(tc):
    n, m = map(int, input().split())
    whiteboard = list(map(int, input().split()))
    opert = list(map(int, input().split()))
    heapq.heapify(whiteboard)
    
    

    for i in  range(m):
        heapq.heappop(whiteboard)
        heapq.heappush(whiteboard, opert[i])
    
    print(sum(whiteboard))

        
