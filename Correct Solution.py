num = list(map(int, input()))
output = input()
num.sort()
zero = num.count(0)
length = len(num)
answer = ''



if length > 1 and num[0] == 0:
    num[0] , num[zero] = num[zero], num[0]


for i in range(length):
    answer += str(num[i])


if answer == output:
    print("OK")
else:
    print("WRONG_ANSWER")