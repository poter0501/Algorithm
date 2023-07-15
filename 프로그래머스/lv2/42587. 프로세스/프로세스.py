from collections import deque

def solution(priorities, location):
    answer = 0
    process_num = deque()
    priority = deque()
    
    for i, pri in enumerate(priorities):
        process_num.append(i)
        priority.append(pri)
    # print(process_num)
    # print(priority)
    
    while process_num:
        process = process_num.popleft()
        pri = priority.popleft()
        
        if len(process_num)==0:
            return answer+1
        
        if pri < max(priority):
            process_num.append(process)
            priority.append(pri)
        else:
            answer+=1
            if process == location:
                return answer
        
    return answer