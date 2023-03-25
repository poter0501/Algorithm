import sys

n, k = map(int, sys.stdin.readline().split())

objects = []
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    objects.append((w, v))

# print(n, k)
# print(objects)

objects.sort(key=lambda x: (x[0], x[1]))
result = [[0 for i in range(k + 1)] for j in range(2)]
for i, w_v in enumerate(objects):
    weight = w_v[0]
    value = w_v[1]
    if weight > k:
        break
    for bag_w in range(1, weight):
        result[(i + 1) % 2][bag_w] = result[i % 2][bag_w]
    for bag_w in range(weight, k + 1):
        result[(i + 1) % 2][bag_w] = max(result[i % 2][bag_w - weight] + value, result[i % 2][bag_w])
print(max(result[0][k], result[1][k]))
