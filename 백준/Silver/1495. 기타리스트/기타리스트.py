import sys
from collections import deque

n, s, m = map(int, sys.stdin.readline().split())

vol = [int(c) for c in sys.stdin.readline().split()]
vol_record = [set() for _ in range(n)]
max_vol = s
result = -1
que = deque([(s, 0)])

while que:
    vol_pre, idx = que.popleft()
    
    if idx < len(vol):
        vol_new1 = vol_pre + vol[idx]
        vol_new2 = vol_pre - vol[idx]
        
        if 0 <= vol_new1 <= m:
            if vol_new1 not in vol_record[idx]:
                que.append((vol_new1, idx + 1))
                vol_record[idx].add(vol_new1)
        if 0 <= vol_new2 <= m:
            if vol_new2 not in vol_record[idx]:
                que.append((vol_new2, idx + 1))
                vol_record[idx].add(vol_new2)
    else:
        result = max(result, vol_pre)
print(result)
