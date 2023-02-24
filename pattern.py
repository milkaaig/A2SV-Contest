testcases = int(input())
word = list(input())
length = len(word)
ans = []

for i in range(length):
    ans.append(word[i])

for i in range(testcases-1):
    compareto = list(input())
    for j in range(length):
        if  compareto[j] != '?':
            if ans[j] != '?' and compareto[j] != ans[j]:
                ans[j] = '1'
            else:
                ans[j] = compareto[j]
               
                
answerstr = ''
for i in range(length):
    if ans[i] == '1':
        answerstr += '?'
    elif ans[i] == '?': 
        answerstr += 'm'
    else:
        answerstr += ans[i]
            
print( answerstr)
             
