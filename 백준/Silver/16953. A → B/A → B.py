import sys

a, b = sys.stdin.readline().rstrip().split()

b_last = b[-1]
count = 1
while len(a) <= len(b):
    
    if b[-1] == '1':
        b = b[:len(b) - 1]
        count += 1
    else:
        if int(b[-1]) % 2 != 0:
            print(-1)
            exit()
        else:
            b = str(int(b) // 2)
            count += 1
    if a == b:
        break

if a != b:
    print(-1)
    exit()
print(count)
