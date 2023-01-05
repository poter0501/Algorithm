import re
from itertools import permutations

def solution(expression):
    answer = 0
    
    reg_num=re.compile('\d')
    reg_op=re.compile('\D')
    
    operator=reg_op.findall(expression)
    op_set=list(set(operator))
    op_odr = list(permutations(op_set,len(op_set)))
    
    express=re.split('(\D)', expression)
    express=list(map(lambda x:int(x) if re.match(reg_num, x) else x, express))
    
    result=[abs(calc(express, o)) for o in op_odr]
    answer=max(result)
    # print(result)
    
    return answer

def calc(express, odrs):
    for op in odrs:
        idx=express.index(op)
        while op in express:
            idx=express.index(op)
            t=0
            if op=='-':
                t=express[idx-1]-express[idx+1]
                express=express[:idx-1] + [t] + express[idx+2:]
            if op=='+':
                t=express[idx-1]+express[idx+1]
                express=express[:idx-1] + [t] + express[idx+2:]
            if op=='*':
                t=express[idx-1]*express[idx+1]
                express=express[:idx-1] + [t] + express[idx+2:]
        
    return express[0]