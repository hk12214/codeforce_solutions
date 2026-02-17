num = int(input())
first_mag = 0
group = 0
for i in range(num):
    magnet= input()
    if magnet != first_mag:
        group +=1
        first_mag = magnet

print(group)
    

