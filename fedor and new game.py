n, m , k = map(int, input().split())
players = []

for i in range(m + 1):
    p = int(input())
    players.append(p)

mine = players.pop()
output = 0

for i in players:
    
    xor = mine ^ i

    count = 0
    shift = 1

    while shift  <= xor:
        if xor & shift != 0:
            count += 1
        
        shift = shift << 1

    if count <= k:
        output += 1

print(output)
