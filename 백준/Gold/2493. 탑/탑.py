import sys
from collections import deque

n = int(sys.stdin.readline())
tower = deque(map(int, sys.stdin.readline().split()))
# n = 5
# tower = [6, 9, 5, 7, 4]
result = [0] * n
stack = []

for i in range(n):
    while stack and stack[-1][1] < tower[i]:
        stack.pop()
    if stack:
        result[i] = stack[-1][0] + 1
    stack.append((i, tower[i]))

print(' '.join(map(str, result)))
