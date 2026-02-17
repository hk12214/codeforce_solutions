n=int(input())
stones=list(map(str,input()))
i=0
j=1
count=0
while j<n:
    if stones[i]==stones[j]:
        count+=1
        i+=1
        j+=1
    else:
        i+=1
        j+=1

print(count)
