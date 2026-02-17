string=str(input())
lower=0
upper=0

for i in range(len(string)):
    if string[i].islower():
        lower+=1
    else:
        upper+=1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())

