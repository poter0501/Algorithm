from collections import deque

def solution(s):
    answer = 0
    for i in range(0, len(s)):
        sub=s[i: ]+s[0:i]
        if is_correct_parenthesis(sub):
            answer+=1
    return answer

def is_correct_parenthesis(s):
    s = deque(s)
    stack = deque()
    while s:
        curr = s.popleft()
        if not stack:
            stack.append(curr)
            continue
        
        if stack[-1]+curr=='()' or stack[-1]+curr=='{}' or stack[-1]+curr=='[]':
            stack.pop()
            continue
        
        stack.append(curr)
            
    return len(s)==0 and len(stack)==0