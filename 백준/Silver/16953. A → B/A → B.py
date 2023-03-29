import sys

a, b = map(int, sys.stdin.readline().split())

count = 1
a_str = str(a)
b_str = str(b)

while True:
    last_digit = b_str[-1]
    if last_digit != '1':
        if int(last_digit) % 2 != 0:
            print(-1)
            exit()
    
    if last_digit == '1':
        count += 1
        b_str = b_str[:-1]
    else:
        count += 1
        b_str = str(int(b_str) // 2)
    
    if b_str == a_str:
        break
    if int(b_str) < a:
        count = -1
        break
        
print(count)
