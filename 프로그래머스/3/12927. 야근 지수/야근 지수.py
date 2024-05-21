import heapq

def solution(n, works):
    answer = 0 
    works=[-1*w for w in works]
    heapq.heapify(works)
    
    for i in range(n):
        if works[0]==0:
            break
        heapq.heapreplace(works, works[0]+1)
    answer=sum(x*x for x in works)
    return answer