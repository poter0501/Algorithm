import sys

n = int(sys.stdin.readline().rstrip())
words = set()
for i in range(n):
    words.add(sys.stdin.readline().rstrip())

result = sorted([i for i in words], key=lambda x: (len(x), x))
for c in result:
    print(c)
