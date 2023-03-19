import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append([int(c) for c in sys.stdin.readline().rstrip()])


def find_can_go(pos):
    x, y, z = pos
    go = [[x, y + 1, z], [x, y - 1, z], [x + 1, y, z], [x - 1, y, z]]
    can_go = []
    for x, y, z in go:
        if 0 <= x < n and 0 <= y < m:
            if board[x][y] != 0:
                can_go.append([x, y, z + 1])
    return can_go


def dfs(pos):
    q = deque([pos])
    while len(q) > 0:
        temp = q.popleft()
        if board[temp[0]][temp[1]] == 1:  # not yet visit and can go
            board[temp[0]][temp[1]] += temp[2]
            for can_go in find_can_go(temp):
                q.append(can_go)


dfs([0, 0, 1])
print(board[n - 1][m - 1] - 1)
