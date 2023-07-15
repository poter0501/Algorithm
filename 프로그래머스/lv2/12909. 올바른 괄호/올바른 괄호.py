from collections import deque

def solution(s):
    answer = True
    if s[0]==")":
        return False
    if s[-1]=="(":
        return False
    
    que = deque()
    
    for pth in s:
        if pth=="(":
            que.append(pth)
        else:
            if que:
                que.pop()
            else:
                return False
    if que:
        return False
    return True