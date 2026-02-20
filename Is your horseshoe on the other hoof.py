s=list(map(int,input().split()))
buy=0
same=[]
for i in range(len(s)):
    if s[i] not in same:
        if s.count(s[i])>1:
            buy+=s.count(s[i])-1
            same.append(s[i])
        
print(buy)
            

        
