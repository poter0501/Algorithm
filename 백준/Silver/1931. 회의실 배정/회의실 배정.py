import sys
from collections import deque

n = int(sys.stdin.readline())

meetings = []
count = 1
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))
# print(meetings)
start, end = meetings[0]
for i in range(1, n):
    start_nxt, end_nxt = meetings[i]
    if end <= start_nxt:
        count += 1
        start = start_nxt
        end = end_nxt
print(count)
