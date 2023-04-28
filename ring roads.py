from collections import defaultdict

n = int(input())
adj = defaultdict(list)

for i in range(n):
    u, v, c = map(int, input().split())
    adj[u].append((v, 0))
    adj[v].append((u, c))

def dfs(ver, par):
    cost = 0
    if ver == 1:
        return cost
    
    for  v, c in adj[ver]:
        if v != par:
            cost += c + dfs(v, ver)
    
    return cost

output = float('inf')
for v , c in adj[1]:
    curr = dfs(v, 1) + c
    output = min(curr,  output)

print(output)

