def solution(n, left, right):
    answer = []
    
    l=left//n
    l_d=left%n
    r=right//n
    count=right-left

    for i in range(l, r+1):
        answer+=[j if (j>i) else i+1 for j in range(1, n+1)]
    answer=answer[l_d: l_d+count+1]
        
    return answer