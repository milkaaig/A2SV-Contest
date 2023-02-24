from collections import defaultdict
testCases = int(input())
 
for _ in range(testCases):
    rd = defaultdict(int)
    ld = defaultdict(int)
    chessboard = []
    rows, columns = list(map(int, input().split()))
    for index in range(rows):
        row = list(map(int, input().split()))
        chessboard.append(row)
        length = len(row)
        for i in range(length):
           rd[index - i] += row[i]
           ld[index + i] += row[i]
    maxi = -1
    for i in range(rows):
        for j in range(columns):
            sum = rd[i-j] + ld[i+j] - chessboard[i][j]
            maxi = max(maxi, sum)
    print(maxi)
