class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        output = []
        size = {i : 1 for i in range(n)}
        rep = {i : i for i in range(n)}

        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            
            return rep[x]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)

            if xrep == yrep:
                return 

            if size[xrep] > size[yrep]:
                rep[yrep] = xrep
                size[xrep] += size[yrep]
            else:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
        

        for i in range(n):
            
            for j in range(i + 1, n):
                val = len(set(accounts[i]).intersection(accounts[j]))

                if val > 1:
                    union(i, j)
        
        org = defaultdict(list)
        for i in range(n):
            val = find(i)
            org[val].append(accounts[i][1 : ])
       
       
        output = []
        for ind, mail in org.items():
            name = [accounts[ind][0]]
            email = []

            for groups in mail:
                email += groups

            email = list(set(email))
            email.sort()
            
            output.append(name + email)
        
        return output