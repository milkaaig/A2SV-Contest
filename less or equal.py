n,k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
out = -1

if k == n:
    out = arr[k - 1]
    
elif 1 <= k < n :
    if arr[k] != arr[k - 1]:
        out = arr[k-1]
elif k==0 and arr[k]>1:
    out = arr[k]-1

    
print(out)
