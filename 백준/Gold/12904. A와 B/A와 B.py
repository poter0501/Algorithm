import sys

s = sys.stdin.readline().rstrip()
t = sys.stdin.readline().rstrip()
# 반대로 생각
# t 문자열의 맨뒤가 b 면 무조건 두번째 연산
# t 문자열의 맨뒤가 a 면 무조건 첫번째 연사
ans = 0
while len(t) >= len(s):
    if t[len(t) - 1] == 'B':
        temp = ''
        for c in range(len(t) - 2, -1, -1):
            temp += t[c]
        t = temp
    elif t[len(t) - 1] == 'A':
        t = t[:len(t) - 1]
    if t == s:
        ans = 1
        break
print(ans)
