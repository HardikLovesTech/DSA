# cook your dish here
n , k = map(int , input().split())
array = list(map(int , input().split()))

found = False

for element in array:
    if element == k:
        found = True
        break
    
if found :
    print('Yes')
else:
    print('No')