import re

def solution(s):
    answer = []
    ss = s[1:len(s)-1]
    
    temp = re.split('\}[,]\{', ss)
    temp[0]=temp[0][1:]
    temp[len(temp)-1]=temp[len(temp)-1][:len(temp[len(temp)-1])-1]
    

    li=[]
    li = list(map(lambda x: x.split(','), temp))

    li2 = sorted(li, key=lambda x: len(x))

    
    for x in li2:
        x = list(map(int, x))
        for y in x:
            if y not in answer:
                answer.append(y)
    
    return answer