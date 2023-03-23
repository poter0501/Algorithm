import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
S, X, Y = map(int, sys.stdin.readline().split())

# print(board)
pos = [[] for i in range(k)]
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            vi = board[i][j]
            pos[vi - 1].append([vi, i, j])
# print(pos)

time = 0
while time < S:
    q = deque(pos)
    pos = [[] for i in range(k)]
    while q:
        temp = q.popleft()
        for vi, x, y in temp:
            # vi, x, y = q.popleft()
            move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for move_x, move_y in move:
                next_x = x + move_x
                next_y = y + move_y
                if 0 <= next_x < n and 0 <= next_y < n:
                    if board[next_x][next_y] == 0:
                        board[next_x][next_y] = vi
                        pos[vi - 1] += [[vi, next_x, next_y]]
    time += 1

print(board[X-1][Y-1])
