import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
stones = [{} for _ in range(n + 1)]  # index i 까지 오는 junp count와 x를 저장
small_stones = set()
for _ in range(m):
    small_stones.add(int(sys.stdin.readline()))
# tt = list(map(int, sys.stdin.readline().split()))
# small_stones = set(tt)

if 2 in small_stones:
    print(-1)
    exit()

stones[2][1] = 1
for i in range(2, n + 1):
    curr = stones[i]
    for x in curr.keys():
        cnt = curr[x]
        if x > 1:
            move = (x, x + 1, x - 1)
        else:
            move = (x, x + 1)
            
        for m in move:
            if i + m not in small_stones and i + m <= n:
                if stones[i + m].get(m, False):
                    stones[i + m][m] = min(stones[i + m][m], cnt + 1)
                else:
                    stones[i + m][m] = cnt + 1

if len(stones[n]) == 0:
    print(-1)
else:
    print(min(stones[n].values()))