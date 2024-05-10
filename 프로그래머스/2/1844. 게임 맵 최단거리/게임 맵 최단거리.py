from collections import deque

def solution(maps):
    history=[[-1 for j in range(len(maps[0]))] for i in range(len(maps))]
    history[0][0]=1
    
    paths=deque([[0,0]])
    while paths:
        curr = paths.popleft()
        x, y = curr
        
        can_move=[(0,1), (0,-1), (1,0), (-1,0)]
        for m_x, m_y in can_move:
            nxt_x=x+m_x
            nxt_y=y+m_y
            if 0<=nxt_x<len(maps) and 0<=nxt_y<len(maps[0]) and maps[nxt_x][nxt_y]==1:
                if history[nxt_x][nxt_y]<0:
                    history[nxt_x][nxt_y]=history[x][y]+1
                    paths.append([nxt_x, nxt_y])
                    continue
                if history[x][y]+1<history[nxt_x][nxt_y]:
                    history[nxt_x][nxt_y]=history[x][y]+1
                    paths.append([nxt_x, nxt_y])
                    continue
        
    return history[len(maps)-1][len(maps[0])-1]