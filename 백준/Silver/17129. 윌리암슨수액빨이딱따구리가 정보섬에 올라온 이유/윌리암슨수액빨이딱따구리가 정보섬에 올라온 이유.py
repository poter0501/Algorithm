import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

board = []
visited = [[0 for i in range(m)] for j in range(n)]
start = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip()))
    for j, r in enumerate(row):
        if r == 2:
            start = [i, j]
            break
    board.append(row)

q = deque([start])
visited[start[0]][start[1]] = 1
min_path = 0
loop = True
while q and loop:
    x, y = q.popleft()
    
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for x_m, y_m in move:
        x_nxt = x + x_m
        y_nxt = y + y_m
        if 0 <= x_nxt < n and 0 <= y_nxt < m:
            if board[x_nxt][y_nxt] != 1 and visited[x_nxt][y_nxt] == 0:
                visited[x_nxt][y_nxt] = visited[x][y] + 1
                q.append([x_nxt, y_nxt])
                if board[x_nxt][y_nxt] != 0 and board[x_nxt][y_nxt] != 1:
                    min_path = visited[x_nxt][y_nxt]
                    loop = False
                    break
if min_path != 0:
    print('TAK')
    print(min_path - 1)
else:
    print('NIE')
