num = int(input())
pr = ""
for i in range(num):
    pr = ""
    str = input()
    str += "?"
    pr += str[0]
    pr += str[1]
    pr +="..."
    print(pr,str)
        
