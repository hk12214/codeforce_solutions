num=int(input())
arr=list(map(str,input()))
A="A"
D="D"
anton=arr.count(A)
danik=arr.count(D)
if anton>danik:
    print("Anton")
elif anton<danik:
    print("Danik")
else:
    print("Friendship")
