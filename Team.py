problem=int(input())
soln=0
for i in range(problem):
    PVT=list(map(int,input().split()))
    one=PVT.count(1)
    zero=PVT.count(0)
    if one>zero:
        soln+=1
print(soln)    
    
