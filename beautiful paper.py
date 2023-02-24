testcases = int(input())
 
for i in range(testcases):
    rect1 = list(map(int,input().split()))
    rect2 = list(map(int,input().split()))
    
    if rect1[0] == rect2[0] and rect1[1] + rect2[1] == rect2[0]:
            print("Yes")
    elif rect1[1] == rect2[1] and rect1[0] + rect2[0] == rect2[1]:
            print("Yes")
    elif rect1[0] == rect2[1] and rect1[1] + rect2[0] == rect2[1]:
            print("Yes")
    elif rect1[1] == rect2[0] and rect1[0] + rect2[1] == rect2[0]:
            print("Yes")
    else:
        print("No")
