from collections import deque

def solution(land):
    
    if len(land)==1:
        return max(land[0])
    history=[[land[i][j] if i==0 else 0 for j in range(4)] for i in range(len(land))]
    
    for i in range(1, len(land)):            
        for j in range(4):
            history[i][j]=land[i][j]+max([history[i-1][k] if k!=j else 0 for k in range(4)])
        
    return max(history[-1])
    