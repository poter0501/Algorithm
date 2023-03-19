import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
edges = [[] for i in range(n)]
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    edges[start - 1] += [end - 1]

visited = [0 for i in range(n)]
min_dist = [float('inf') for i in range(n)]
q = deque()
q.append([x - 1, 0])

while len(q) > 0:
    temp = q.popleft()
    if visited[temp[0]] == 0:
        visited[temp[0]] = 1
        min_dist[temp[0]] = min(min_dist[temp[0]], temp[1])
        for can_go in edges[temp[0]]:
            q.append([can_go, temp[1] + 1])

count = 0
for i, dist in enumerate(min_dist):
    if dist == k:
        print(i + 1)
        count += 1
if count == 0:
    print(-1)
