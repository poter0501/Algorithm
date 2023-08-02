import sys
from collections import deque

left = deque()
right = deque(sys.stdin.readline().rstrip())
window = deque()

explore = sys.stdin.readline().rstrip()

while True:
    if len(window) < len(explore):
        if right:
            window.append(right.popleft())
        else:
            break
    if len(window) == len(explore):
        if ''.join(window) == explore:
            window = deque()
            while left and len(window) < len(explore) - 1:
                window.appendleft(left.pop())
        else:
            left.append(window.popleft())
    
    if len(left) + len(window) + len(right) < len(explore):
        break
    if not right:
        break

if not left and not window and not right:
    print('FRULA')
else:
    print(''.join(left) + ''.join(window) + ''.join(right))
