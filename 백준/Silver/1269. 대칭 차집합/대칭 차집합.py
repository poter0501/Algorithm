import sys

n, m = map(int, sys.stdin.readline().split())
a = set(list(map(int, sys.stdin.readline().split())))
b = set(list(map(int, sys.stdin.readline().split())))

c = (a - b).union(b-a)
print(len(c))
