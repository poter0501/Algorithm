import sys

d, k = map(int, sys.stdin.readline().split())

a = [0 for i in range(d + 1)]
b = [0 for i in range(d + 1)]
a[1] = 1
a[2] = 1

b[1] = 1
b[2] = 2

for day in range(3, d + 1):
    a[day] = a[day - 1] + a[day - 2]
    b[day] = b[day - 1] + b[day - 2]

A = a[day - 2]
B = b[day - 2]
temp_k = k
ans_a = 1
ans_b = 1
while True:
    temp_k -= A * ans_a
    if temp_k % B == 0:
        ans_b = temp_k // B
        break
    temp_k = k
    ans_a += 1

print(ans_a)
print(ans_b)
