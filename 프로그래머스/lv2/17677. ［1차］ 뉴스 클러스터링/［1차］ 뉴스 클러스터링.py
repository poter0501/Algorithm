import re
import math
def solution(str1, str2):
    answer = 0
    regex = re.compile('[a-zA-Z][a-zA-Z]')
    
    str1_li=[str1[i:i+2].lower() for i in range(len(str1)-1) if regex.match(str1[i:i+2])!=None]
    str2_li=[str2[i:i+2].lower() for i in range(len(str2)-1) if regex.match(str2[i:i+2])!=None]
    
    intersection_num=0
    tt=[]
    for i, s in enumerate(str1_li):
        if s in str2_li:
            tt.append(i)
            str2_li.remove(s)
            intersection_num+=1
            
    union_num=len(str1_li)+len(str2_li)
    if union_num==0 and intersection_num==0:
        answer=65536
    else:
        if union_num!=0:
            answer=math.floor((intersection_num/union_num)*65536)
    return answer