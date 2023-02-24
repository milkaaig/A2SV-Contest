testcases = int(input())
for i in range(testcases):
    size, k = list(map(int, input().split()))
    output = 0
    a = list(map(int, input().split()))
    count = 0
    for i in range(size - 1):
        if a[i] < 2 * a[i+1]:
            count += 1
        else:
            count = 0

        if count == k:
            output += 1
            count -= 1
    print(output)
