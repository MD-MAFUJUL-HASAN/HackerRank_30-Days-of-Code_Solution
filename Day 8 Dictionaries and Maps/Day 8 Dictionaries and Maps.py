# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
d = {}

for i in range(n):
    x = input().split()
    d[x[0]] = x[1]

while True:
    try:
        NAME = input()
        if NAME in d:
            print(NAME, "=", d[NAME], sep="")
        else:
            print("Not found")
    except:
        break
