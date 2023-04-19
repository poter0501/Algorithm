import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().rstrip())
relationship = [[] for i in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    relationship[x].append(y)
    relationship[y].append(x)

counted = set()
que = deque([(a, 0)])
answer = -1
while que:
    curr, count = que.popleft()
    
    for p in relationship[curr]:
        if p not in counted and p != a:
            if p == b:
                answer = count + 1
                break
            que.append((p, count + 1))
            counted.add(p)
print(answer)
