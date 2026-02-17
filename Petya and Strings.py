string1=str(input())
string2=str(input())
if string1.upper() < string2.upper():
    print(-1)
elif string1.upper() > string2.upper():
    print(1)
else:
    print(0)
