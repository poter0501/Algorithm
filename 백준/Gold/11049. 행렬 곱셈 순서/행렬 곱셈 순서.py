import sys

n = int(sys.stdin.readline())
dp = [[0 if i <= j else float('inf') for i in range(n)] for j in range(n)]

nums = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if _ != n - 1:
        nums.append(a)
    else:
        nums.append(a)
        nums.append(b)

# print(nums)

i = 0
j = 1
og = [i, j]
while True:
    if i == 0 and j == n:
        break
    try:
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1])
        i += 1
        j += 1
    except IndexError:
        i = 0
        j = og[1] + 1
        og = [i, j]

print(dp[0][n - 1])
