def solution(arr1, arr2):
    a, b, c = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0 for j in range(c)] for i in range(a)]
    
    for i in range(a):
        for j in range(c):
            for k in range(b):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer
    
    
    
    
            