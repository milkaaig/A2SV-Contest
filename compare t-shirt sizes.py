testcases = int(input())
for i in range(testcases):
    compare = input().split()
    l = str(compare[0])
    r = str(compare[1])
    if l == r:
        print('=')
    else:
        if l == 'M':
            if 'S' in r:
                print('>')
            else:
                print('<')
        elif r == 'M':
            if 'S' in l:
                print('<')
            else:
                print('>')
        elif 'L' in l:
            if 'L' not in r:
                print('>')
            elif l.count('X') > r.count('X'):
                print('>')
            else:
                print('<')
        elif 'L' in r:
            if 'L' not in l:
                print('<')
            elif l.count('X') < r.count('X'):
                print('<')
            else:
                print('>')
        elif 'S' in l:
            if 'S' not in r:
                print('<')
            elif l.count('X') > r.count('X'):
                print('<')
            else:
                print('>')
        elif 'S' in r:
            if 'S' not in l:
                print('>')
            elif l.count('X') > r.count('X'):
                print('<')
            else:
                print('>')
