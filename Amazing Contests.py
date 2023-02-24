numcont = int(input())
codpoints = list( map(int, input().split() ))
length = len(codpoints)
count = 0


minn = codpoints[0]
maxx = codpoints[0]
for i in range(1,length):
    if codpoints[i] > maxx:
        maxx =codpoints[i]
        count += 1
    elif codpoints[i] < minn:
        minn = codpoints[i]
        count += 1
print(count)

