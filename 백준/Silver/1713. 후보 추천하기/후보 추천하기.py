import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
count = int(sys.stdin.readline().rstrip())
students = list(map(int, sys.stdin.readline().split()))
candi = []
for i, stdt in enumerate(students):
    if len(candi) < n:
        do_add = False
        for j, can in enumerate(candi):
            c, count, order = can
            if c == stdt:
                candi[j][1] += 1
                do_add = True
                break
        if not do_add:
            candi.append([stdt, 1, i])
    else:
        do_add = False
        for j, can in enumerate(candi):
            c, count, order = can
            if c == stdt:
                candi[j][1] += 1
                do_add = True
                break
        if not do_add:
            candi.sort(key=lambda x: (x[1], x[2]))
            candi[0] = [stdt, 1, i]

candi.sort(key=lambda x: x[0])
ans = [s[0] for s in candi]
print(' '.join(map(str, ans)))

