name=input().lower()
rotation=0
sample="a"
for i in name:
    dis=abs(ord(sample)-ord(i))
    if dis< 26-dis:
        rotation+=dis
    else:
        rotation+=26-dis
    sample=i
print(rotation)
        

