import sys

a = [c for c in sys.stdin.readline().rstrip()]
b = [c for c in sys.stdin.readline().rstrip()]

result = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]

for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        aa = a[j - 1]
        bb = b[i - 1]
        if aa == bb:
            result[i][j] = result[i - 1][j - 1] + 1
        else:
            result[i][j] = max(result[i - 1][j], result[i][j - 1])

i = len(b)
j = len(a)
temp = result[i][j]
count = 0
while True:
    if result[i - 1][j] == temp:
        i = i - 1
    elif result[i][j - 1] == temp:
        j = j - 1
    else:
        i = i - 1
        j = j - 1
        count += 1
    temp = result[i][j]
    if temp == 0:
        break
print(count)