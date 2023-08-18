import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(m):
    graph.append([c for c in sys.stdin.readline().rstrip()])

visited = [[False for _ in range(n)] for __ in range(m)]
score_dict = {'W': 0, 'B': 0}
move = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y, side):
    que = deque([[x, y]])
    count = 0
    while que:
        x, y = que.popleft()
        if not visited[x][y] and graph[x][y] == side:
            count += 1
            visited[x][y] = True
            for move_x, move_y in move:
                nxt_x = x + move_x
                nxt_y = y + move_y
                if 0 <= nxt_x < m and 0 <= nxt_y < n:
                    if not visited[nxt_x][nxt_y] and graph[nxt_x][nxt_y] == side:
                        que.append([nxt_x, nxt_y])
    return count


for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            side = graph[i][j]
            count = bfs(i, j, side)
            score_dict[side] += count ** 2

print(f'{score_dict["W"]} {score_dict["B"]}')
