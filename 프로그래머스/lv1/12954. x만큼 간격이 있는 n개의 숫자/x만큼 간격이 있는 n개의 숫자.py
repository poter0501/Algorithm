def solution(x, n):
    return [i for i in range(x, x+n*x, x)] if x!=0 else [0 for i in range(n)]