x , y, z = tuple(map(int , input().split()))
temp = 0
if x > y:
    temp = x
    x = y
    y = temp
if x > z:
    temp = x
    x = z
    z = temp
if y > z:
    temp = y
    y = z
    z = temp
print(x, y, z)