class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equations.sort(key = lambda x : x[1], reverse = True)
        rep = {chr(i) : chr(i) for i in range(97, 97 + 26)}
        
        n = len(equations)
        
        def find(x):
            if rep[x] == x:
                return x
            root = find(rep[x])
            rep[x] = root

            return root

        def union(x, y):
            xrep = find(rep[x])
            yrep = find(rep[y])

            if xrep == yrep:
                return
            
            rep[yrep] = xrep
            
        for i in range(n):
            if equations[i][1] == "=":
                union(equations[i][0], equations[i][3])
            else:
                
                x = find(equations[i][0])
                y = find(equations[i][3])
               
                if x == y:
                    return False
        
        return True