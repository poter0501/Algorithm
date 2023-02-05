def solution(s):
    answer = [0,0]
    answer = recursive_func(s, answer)
    
    return answer

def recursive_func(s, answer):
    result = answer
    if s=='1':
        return result
    else:
        temp = bin(len(s.replace('0','')))[2:]
        result = recursive_func(temp, [result[0]+1, result[1]+s.count('0')])
        return result
        
        
        