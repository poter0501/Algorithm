import sys

equation_str = sys.stdin.readline().rstrip()
temp = equation_str.split('-')
length = len(temp)
ans = 0
for _ in range(length):
    right_side = temp.pop()
    try:
        if len(temp) != 0:
            ans += eval(right_side)
        else:
            ans -= eval(right_side)
    except SyntaxError:
        temp_part = right_side.split('+')
        temp_part = list(map(int, temp_part))
        if len(temp_part) == 1:
            right_side = str(temp_part[0])
        else:
            right_side = '+'.join(map(str, temp_part))
            
        if len(temp) != 0:
            ans += eval(right_side)
        else:
            ans -= eval(right_side)

print(-ans)
