nb = int(input())
boys = list(map (int, input().split()))
ng = int(input())
girls = list(map (int, input().split()))
count = 0
boys.sort()
girls.sort()

i = 0
j = 0
while i < ng and j < nb:
    if boys[j] == girls[i] or abs(boys[j] - girls[i] ) == 1:
        i += 1
        j += 1
        count += 1
    elif boys[j] < girls[i]:
        j += 1
    elif girls[i] < boys[j]:
        i += 1
print(count)
