stones= list(map(str,input()))
instraction=list(map(str,input()))
position=0
for i in range(len(instraction)):
    if instraction[i]==stones[position]:
        position+=1
print(position+1)
