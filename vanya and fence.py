a,b=map(int,input().split())
arr=list(map(int,input().split()))
W=0
for i in range(int(a)):
    if arr[i]<=int(b):
        W+=1
    else:
        W+=2
print (W)
