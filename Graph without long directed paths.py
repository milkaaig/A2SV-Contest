from collections import defaultdict
import sys, threading

def main():

    n, m = map(int, input().split())
    graph = defaultdict(list)
    edge = []
    for i in range(m):
        u,v = map(int, input().split())
        edge.append((u, v ))
        graph[u].append((v, i))
        graph[v].append((u, i))

    visited = defaultdict(int)
    source , sink = 1, 2
    ans = [0] * m

    def dfs(ver, prev):
        visited[ver] = curr = prev ^ 3
        
        
        for v, i in graph[ver]:
            if curr == source and edge[i][0] != ver:
                ans[i] = 1
            elif curr == sink and edge[i][1] != ver:
                ans[i] = 1
                
            if v  not in visited:
                if not  dfs(v, curr):
                    return False
            elif visited[v] == curr:
                return False
        
        return True


    if dfs(1, 1):
        print("YES")
        print(*ans, sep = '')
    else:
        print("NO")

sys.setrecursionlimit(1 << 30)
threading.stack_size(100000000)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()

        

