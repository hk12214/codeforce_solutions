num = int(input())
cards = list(map(int,input().split()))
Sereja = 0
Dima = 0
p1=0
p2=num-1
while p1<=p2:

    if cards[p1]>cards[p2]:
        Sereja+=cards[p1]
        p1+=1
    else:
        Sereja+=cards[p2]
        p2-=1
    
    if p1<=p2:
        if cards[p1]>cards[p2]:
            Dima+=cards[p1]
            p1+=1
        else:
            Dima+=cards[p2]
            p2-=1
    
print(Sereja, Dima)

