def solution(dirs):
    answer = 0
    mov={"U":(0,1), "D":(0,-1), "L":(-1,0), "R":(1,0)}
    curr=[0,0]
    path= set()
    for m in dirs:
        mov_x, mov_y = mov[m]
        nxt_x= curr[0]+mov_x
        nxt_y= curr[1]+mov_y
        if -5<=nxt_x<=5 and -5<=nxt_y<=5:
            path.add(path_str(curr, [nxt_x, nxt_y], m))
            curr=[nxt_x, nxt_y]
    return len(path)

def path_str(curr, nxt, direction):
    if direction=='U' or direction=='R':
        return str(curr[0])+str(curr[1])+direction
    if direction=='D':
        return str(nxt[0])+str(nxt[1])+'U'
    if direction=='L':
        return str(nxt[0])+str(nxt[1])+'R'