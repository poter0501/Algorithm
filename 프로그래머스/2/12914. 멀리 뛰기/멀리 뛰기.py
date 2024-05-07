def solution(n):
    answer = 0
    result = [0, 1, 2]
    if n<=2:
        return result[n]
    for i in range(3, n+1):
        result.append(result[i-1]+result[i-2])
    return result[n]%1234567