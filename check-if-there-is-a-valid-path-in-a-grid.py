class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        street = {1 : [(), (1, 3, 5 )], 2 : [(2, 5, 6), ()], 3 : [(2, 5, 6),()], 4 :[ (2, 5, 6), (1, 3, 5)], 5:[(), ()], 6 : [(), (1, 3, 5)]}

        size = {}
        rep = {}
        row, col = len(grid), len(grid[0])

        inbound = lambda x, y: x in range(row) and y in range(col)

        def find(x):
            if x not in rep:
                rep[x] = x
                size[x] = 1
                return x


            if rep[x] != x:
                root = find(rep[x])
                rep[x] = root
            
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
        
        for i in range(row):
            for j in range(col):
                rr, rc = i, j + 1
                dr, dc = i + 1, j

                if  inbound(rr, rc) and  grid[rr][rc] in street[grid[i][j]][1]:
                    union((rr, rc), (i, j))
                if inbound(dr, dc) and grid[dr][dc] in street[grid[i][j]][0]:
                    union((dr, dc), (i, j))
        
        return find((0, 0)) == find((row - 1, col - 1))