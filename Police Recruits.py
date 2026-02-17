n=int(input())
num=list(map(int,input().split()))
police=0
crime=0
inv=0
for i in range(n):
    if num[i] == -1:
        if police>0:
            police-=1
        else:
            crime+=1
    else:
        police+=num[i]
print(crime)        
        
    
    
