def solution(answers):
    answer = []
    temp1 = [1, 3, 4, 5]
    temp2 = [3, 1, 2, 4, 5]
    
    student0= [ n%5 +1 for n in range(len(answers))]
    student1= [ 2 if n%2==1 else (temp1[((n//2)-1)%4]) for n in range(1, len(answers)+1)]
    student2= [ temp2[(n//2)%5] for n in range(len(answers))]
    
    correct = [0, 0, 0]
    
    for i, ans in enumerate(answers):
        if student0[i] == ans:
            correct[0]+=1
        if student1[i] == ans:
            correct[1]+=1
        if student2[i] == ans:
            correct[2]+=1
            
    max_cor = max(correct)
    
    if max_cor == 0:
        return answer
    
    for i, count in enumerate(correct):
        if count == max_cor:
            answer.append(i+1)
    
    answer.sort()
    
    return answer