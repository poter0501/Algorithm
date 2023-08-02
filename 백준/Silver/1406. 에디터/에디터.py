import sys
from collections import deque

left = deque(sys.stdin.readline().rstrip())
right = deque()
n = int(sys.stdin.readline())

for _ in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'L' and len(left) != 0:
        right.appendleft(left.pop())
    elif cmd[0] == 'D' and len(right) != 0:
        left.append(right.popleft())
    elif cmd[0] == 'B' and len(left) != 0:
        left.pop()
    elif cmd[0] == 'P':
        left.append(cmd[1])

print(''.join(left) + ''.join(right))
