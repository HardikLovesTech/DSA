# cook your dish here
n = int(input())
pairs = []
for _ in range(n):
    no = tuple(map(int , input().split()))
    pairs.append(no)

a, b = map(int, input().split())

found = False

for x , y in pairs:
    if (x == a and y == b) or (x == b and y == a):
        found = True
        break
if found:
    print("YES")
else:
    print("NO")