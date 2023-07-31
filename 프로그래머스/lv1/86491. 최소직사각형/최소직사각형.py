def solution(sizes):
    answer = 0
    width = float('-inf')
    height = float('-inf')
    for w, h in sizes:
        if h>w:
            temp = w
            w = h
            h = temp
        width = max(width, w)
        height = max(height, h)
    print(f"w= {width}, h= {height}")
    answer=width*height
    
    return answer