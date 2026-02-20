y, w = map(int, input().split())

point = [1,2,3,4,5,6]
max_point = max(y, w)

dot = point[max_point-1:]
leng = len(dot)

numerator = leng
denominator = 6

g = math.gcd(numerator, denominator)

numerator //= g
denominator //= g

print(str(numerator) + "/" + str(denominator))
