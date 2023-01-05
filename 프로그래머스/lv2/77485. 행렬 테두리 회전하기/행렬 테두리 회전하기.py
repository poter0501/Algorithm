def solution(rows, columns, queries):
    arr = [[(i+1)+(j*columns) for i in range(columns)] for j in range(rows)]
    answer = []
    
    for q in queries:
        t=rotation(arr, q)
        arr=t[0]
        answer.append(t[1])
    return answer

def rotation(arr, q):
    coord=[]
    val=[]
    minimun = 0
    
    coord=[[q[0]-1, j-1] for j in range(q[1], q[3]+1)]
    coord+=[[i-1, q[3]-1] for i in range(q[0]+1, q[2]+1)]
    coord+=[[q[2]-1, j-1] for j in range(q[3]-1, q[1]-1,-1)]
    coord+=[[i-1, q[1]-1] for i in range(q[2]-1, q[0], -1)]
    
    val = list(map(lambda x: arr[x[0]][x[1]], coord))
    minimum=min(val)
     
    temp = val.pop()
    val.insert(0, temp)
    for i, x in enumerate(coord):
        arr[x[0]][x[1]] = val[i]
        
    return (arr, minimum)