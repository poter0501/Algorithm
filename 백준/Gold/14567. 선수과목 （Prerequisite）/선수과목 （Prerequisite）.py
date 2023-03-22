import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

in_degree = [0 for i in range(n + 1)]
edge = [set() for i in range(n + 1)]
for _ in range(m):
    pre, cur = map(int, sys.stdin.readline().split())
    edge[pre].add(cur)
    in_degree[cur] += 1

# print(in_degree)
# print(edge)

q = deque()
for i in range(1, n + 1):
    if in_degree[i] == 0:
        q.append([i, 1])

result = [0 for i in range(n + 1)]
while q:
    temp, semester = q.popleft()
    result[temp] = semester
    
    for nxt in edge[temp]:
        if in_degree[nxt] > 0:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append([nxt, semester + 1])

print(' '.join(map(str, result[1:])))