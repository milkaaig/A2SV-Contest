class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        rep = {chr(i) : chr(i) for i in range(97, 97 + 26)}
        n = len(s1)

        def find(x):
            if rep[x] != x:
                root = find(rep[x])
                rep[x] = root
            
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)

            if xrep != yrep:
                if xrep < yrep:
                    rep[yrep] = xrep
                else:
                    rep[xrep] = yrep
        
        for i in range(n):
            union(s1[i], s2[i])
        
        output = ''
        for letter in baseStr:
            output += find(letter)

        return output