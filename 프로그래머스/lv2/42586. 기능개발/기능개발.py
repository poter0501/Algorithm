import math

def solution(progresses, speeds):
    answer = []
    
    days=[]
    for i,p in enumerate(progresses):
        x = (100-p)/speeds[i]
        days.append(math.ceil(x))
    print(days)
    
    count=1;
    d = days[0]
    while len(days)>1:
        del days[0]
        
        if d>=days[0]:
            count+=1
        else:
            d = days[0]
            answer.append(count)
            count=1
            
    answer.append(count)
    
    return answer