from collections import defaultdict

n = int(input())
masks = defaultdict(int)
count = 0

for _ in range(n):
    string = input()
    mask = 0

    for char in string:
        diff = ord(char) - ord('a')
        mask ^= 1 << diff

    count += masks[mask]
    masks[mask] += 1

    for i in range(26):
        check = mask ^ (1 << i)
        count += masks[check]

print(count)

        
        



