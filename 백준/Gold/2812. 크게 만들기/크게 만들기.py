import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
num = deque([i for i in str(sys.stdin.readline().rstrip())])

stack = []
pop_count = 0
for i, number in enumerate(num):
    while True:
        if stack and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(number)
if k > 0:
    print(''.join(map(str, stack[:-k])))
else:
    print(''.join(map(str, stack)))
