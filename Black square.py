a1,a2,a3,a4=map(int,input().split())
s=str(input())
Total=0
for i in range(len(s)):
    if s[i]=="1":
        Total+=a1
    elif s[i]=="2":
        Total+=a2
    elif s[i]=="3":
        Total+=a3
    elif s[i]=="4":
        Total+=a4

print(Total)
        
