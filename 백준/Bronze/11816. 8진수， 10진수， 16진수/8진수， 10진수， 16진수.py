import sys

n = sys.stdin.readline().rstrip()

if n[0] == '0':
    if n[1]!='x':
        n = n[0] + 'o' + n[1:]
        print(int(n, 8))
    else:
        print(int(n, 16))
else:
    print(n)
