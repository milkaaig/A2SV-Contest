class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep = {i : i for i in range(1, n + 1)}
        size = {i : 1 for i in range(1, n + 1)}
       
        def find(x):
            if rep[x] == x:
                return x
            
            root = find(rep[x])
            rep[x] = root
            
            return root

        def union(x, y):
            xrep = find(x)
            
            yrep = find(y)

            if xrep == yrep:
                return
            
            print(xrep, yrep)
            if size[xrep] > size[yrep]:
                rep[yrep] = xrep
                size[xrep] += size[yrep]

            else:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
            
                
                
                
        for i, j, k in roads:
            union(i, j)
        
        dist = float("inf")
        for i, j, k in roads:
            if find(1) == find(i):
                dist = min(k, dist)
              
       
            
            

        return dist