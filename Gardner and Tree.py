from collections import *

tc = int(input())


for i in range(tc):

    graph = defaultdict(list)
    degree = defaultdict(int)
    
    x = input()
    nodes, k = map(int, input().split())

    for  i in range(nodes - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    q = deque()
    count = 0

    for i in range(1, nodes + 1):
        if degree[i] <= 1:
            q.append(i)
         
            

    
    while q and k > 0:

        n = len(q)

        for i in range(n):
            ver = q.popleft()
            count += 1
            
            for child in graph[ver]:
                degree[child] -= 1

                if degree[child] == 1:
                    q.append(child)
                       
                        
        
        k -= 1
   
    print(nodes - count)
        




    
