testcases = int(input())
for i in range(testcases):
    distinct = []
    distinct = list(map(int,input().split()))
    big = max(distinct)
    small = min(distinct)
    for i in distinct:
        if i != big and i != small:
            print(i)
