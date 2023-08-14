import sys

n = int(sys.stdin.readline())

pattern = [[' ' for _ in range(n)] for __ in range(n)]


def fill_pattern(start_i, start_j, num):
    if num == 3:
        for i in range(3):
            for j in range(3):
                if not (i == 1 and j == 1):
                    pattern[start_i + i][start_j + j] = '*'
    else:
        window_size = num // 3
        for i in range(num//window_size):
            for j in range(num//window_size):
                if not (i == 1 and j == 1):
                    fill_pattern(start_i+window_size*i, start_j+window_size*j, window_size)


fill_pattern(0, 0, n)
for p in pattern:
    print(''.join(p))
