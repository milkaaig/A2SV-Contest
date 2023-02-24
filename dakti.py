num = int(input())
for i in range(num):
    ordered = {}
    lyrics = input().split()
    lenly = len(lyrics)
   
    for  word in lyrics:
        output = ""
        order = ''
        for letter in word:
            if  letter.isdigit() != True:
                output += letter
            else:
               order =  int(letter)
        ordered[order] = output
    
    orderkeys = list(ordered.keys())
    orderkeys.sort()
    lyricsdic = [ ordered[n] for n in orderkeys]
    print(*lyricsdic)
