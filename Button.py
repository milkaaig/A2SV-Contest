tc = int(input())

for i in range(tc):
    flag = 0
    output = set()
    strs = input()
    size = len(strs)
    if size == 1:
        output.add(strs)
    else:
        s = list(strs)
        i = size-1
        while i >= 0:
            if i -1 < 0:
                output.add(s[i])
                break
            if s[i] == s[i - 1]:
                i -= 2
            elif s[i] != s[i -1]:
                output.add(s[i])
                
                i -= 1
    l = sorted(output)
    print(*l,sep='')
