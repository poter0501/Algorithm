import sys
from collections import deque

k = int(sys.stdin.readline())

global edge
global visited


def bfs(curr):
    que = deque([[curr, 1]])
    
    while que:
        temp = que.popleft()
        if visited[temp[0] - 1] == 0:
            visited[temp[0] - 1] = temp[1]
            can_go = edges[temp[0]]
            for go in can_go:
                que.append([go, 2 if temp[1] == 1 else 1])


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    edges = {i: set() for i in range(1, v + 1)}
    edges_list = []
    visited = [0 for i in range(v)]  # 0: not yet
    is_yes = True
    for _ in range(e):
        x, y = map(int, sys.stdin.readline().split())
        edges[x].add(y)
        edges[y].add(x)
        edges_list.append([x, y])
    # print()
    # print(f'v={v}, e={e}')
    # print(edges)
    while True:
        try:
            bfs(visited.index(0)+1)
        except ValueError:
            break
    for a, b in edges_list:
        if visited[a - 1] == visited[b - 1]:
            print('NO')
            is_yes = False
            break
    if is_yes:
        print('YES')
