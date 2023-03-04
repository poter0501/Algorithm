import sys

short_guys = []
for i in range(9):
    short_guys.append(int(sys.stdin.readline()))

short_guys.sort()
total = sum(short_guys)
fake_short_guys_idx = set()

loop = True
for i in range(len(short_guys)):
    if short_guys[i] < total - 100:
        for j in range(i + 1, len(short_guys)):
            if short_guys[i] + short_guys[j] == total - 100:
                fake_short_guys_idx.add(i)
                fake_short_guys_idx.add(j)
                loop = False
                break
        if not loop:
            break

for i, short_guy in enumerate(short_guys):
    if i not in fake_short_guys_idx:
        print(short_guy)
