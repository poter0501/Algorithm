from collections import deque

def solution(prices):
    answer = []
    que = deque(prices)
    
    while que:
        time = 0
        stock = que.popleft()
        for stk in que:
            if stk >= stock:
                time+=1
            else:
                time+=1
                break
                
        answer.append(time)
    # print(answer)
    return answer