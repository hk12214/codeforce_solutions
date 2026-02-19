k,r=map(int,input().split())
shovel=0
i=1
while shovel==0 :
    if k*i %10==0:
        shovel=i
    elif (k*i-r)%10==0:
        shovel=i
    i+=1
print(shovel)
        
