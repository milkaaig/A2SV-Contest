class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rep = {i : i for i in range(n)}
        size = {i : 1 for i in range(n)}

        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)

            if xrep != yrep:
                if size[xrep] > size[yrep]:
                    rep[yrep] = xrep
                    size[xrep] += size[yrep]
                else:
                    rep[xrep] = yrep
                    size[yrep] += size[xrep]

        
        for  i in range(n):
            x, y = stones[i]
            for j in range(i + 1, n):
                w, z = stones[j]
                if x == w or y == z:
                    union(i, j)
        
        for i in range(n):
            find(i)
        
        return n - len(set(rep.values()))