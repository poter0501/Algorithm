n = int(input())
answer = 1
for i in [k for k in range(1, n + 1)]:
    answer = answer * i
print(answer)