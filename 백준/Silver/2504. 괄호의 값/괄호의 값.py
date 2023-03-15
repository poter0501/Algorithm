import sys

ps = list(map(str, sys.stdin.readline().rstrip()))
# print(ps)
result = 0
stack = []
temp = 1
for i, c in enumerate(ps):
    if c == '(':
        stack.append(c)
        temp *= 2
    elif c == '[':
        stack.append(c)
        temp *= 3
    elif c == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if ps[i - 1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] != '[':
            result = 0
            break
        if ps[i - 1] == '[':
            result += temp
        temp //= 3
        stack.pop()

if stack:
    print(0)
else:
    print(result)
