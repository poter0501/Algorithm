def solution(triangle):
    answer = 0
    temp=[triangle[i] for i in range(len(triangle)-1, -1, -1)]
    for i in range(len(temp)-1):
        for j in range(len(temp[i])-1):
            max= temp[i][j]
            
            if max<temp[i][j+1]:
                max=temp[i][j+1]
                
            temp[i+1][j]+=max
            
    answer = temp[len(temp)-1][0]
    return answer