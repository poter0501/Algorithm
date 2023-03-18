import copy
import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
visited = [0 for _ in range(n + 1)]
edges = {}
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    if edges.get(start, False):
        edges[start].add(end)
    else:
        edges[start] = set([end])
    
    if edges.get(end, False):
        edges[end].add(start)
    else:
        edges[end] = set([start])

# 중복 제거 및 오름차순 정렬
for k in edges.keys():
    edges[k] = sorted(list(edges[k]))

path = []


def dfs(current):
    if visited[current] != 0:  # 이미 순회 한곳
        return
    else:  # 아직 순회 하지 않은곳
        visited[current] = current
        path.append(current)
        if edges.get(current, False):
            for go in edges[current]:
                dfs(go)
        return


def bfs(current):
    q = deque([current])
    while len(q) > 0:
        temp = q.popleft()
        if visited[temp] == 0:  # 아직 순회 하지 않은곳
            visited[temp] = current
            path.append(temp)
            if edges.get(current, False):
                for e in edges[temp]:
                    q.append(e)


dfs(v)
print(' '.join(map(str, path)))

path = list()
visited = [0 for _ in range(n + 1)]

bfs(v)
print(' '.join(map(str, path)))