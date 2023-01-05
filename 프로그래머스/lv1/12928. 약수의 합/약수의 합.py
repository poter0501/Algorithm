import math

def solution(n):
    temp = set()
    answers = set()
    
    for i in range(1,int(math.sqrt(n)+1),1):
        print(i)
        if n%i ==0:
            temp.add(i)
            answers.add(i)
                    
    for i in temp:
        if n%i==0:
            answers.add(n//i)
    
    return sum(answers)