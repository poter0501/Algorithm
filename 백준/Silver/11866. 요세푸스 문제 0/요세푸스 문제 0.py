import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
people = [i for i in range(1, n + 1)]
# print(people)
result = []

for _ in range(n):
    if k > len(people):
        circle_idx = k % len(people)
        result.append(people[circle_idx - 1])
        if circle_idx == 0 and len(people) >= 1:
            people = people[:len(people)-1]
        elif circle_idx == 1:
            people = people[circle_idx:]
        else:
            people = people[circle_idx:] + people[:circle_idx - 1]
    else:
        result.append(people[k - 1])
        people = people[k:] + people[:k - 1]

print('<' + ', '.join(list(map(str, result))) + '>')
