# Enter your code here. Read input from STDIN. Print output to STDOUT

T = int(input())
for i in range(T):
    s = str(input())
    even = [s[i] for i in range(0, len(s), 2)]
    odd = [s[i] for i in range(1, len(s), 2)]
    even = ''.join(even)
    odd = ''.join(odd)
    print("{} {}".format(even, odd))

