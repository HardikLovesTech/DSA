# cook your dish here
string = input()
char = input()

position = -1 

for i in range(len(string)):
    if string[i] == char:
        position = i
        break
print(position)