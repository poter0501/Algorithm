import sys
from collections import deque

idx = 1
while True:
    n = int(sys.stdin.readline())
    dp = [[0 for i in range(n)] for j in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    if n == 0:
        break
    cave = []
    for _ in range(n):
        cave.append(list(map(int, sys.stdin.readline().split())))
    
    # print(cave)
    que = deque([[0, 0]])
    dp[0][0] = cave[0][0]
    visited[0][0] = True
    
    while que:
        x, y = que.popleft()
        
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for x_move, y_move in move:
            x_nxt = x + x_move
            y_nxt = y + y_move
            if 0 <= x_nxt < n and 0 <= y_nxt < n:
                if visited[x_nxt][y_nxt]:
                    if dp[x_nxt][y_nxt] > dp[x][y] + cave[x_nxt][y_nxt]:
                        que.append([x_nxt, y_nxt])
                        dp[x_nxt][y_nxt] = min(dp[x_nxt][y_nxt], dp[x][y] + cave[x_nxt][y_nxt])
                else:
                    que.append([x_nxt, y_nxt])
                    dp[x_nxt][y_nxt] = dp[x][y] + cave[x_nxt][y_nxt]
                    visited[x_nxt][y_nxt] = True
    # print()
    print(f'Problem {idx}: {dp[n - 1][n - 1]}')
    idx += 1
