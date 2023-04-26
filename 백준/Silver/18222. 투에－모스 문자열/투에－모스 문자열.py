import sys

k = int(sys.stdin.readline().rstrip())

def recursive_func2(n):
    if n == 1:
        return '1'
    elif n == 0:
        return '0'
    else:
        tt = len(str(bin(n))[2:])  # 2^(temp-1) <= k < 2^temp
        half_size = 2 ** (tt-1)
        dist = n - half_size
        midterm = recursive_func2(dist)
        if midterm == '1':
            return '0'
        else:
            return '1'


print(recursive_func2(k-1))
