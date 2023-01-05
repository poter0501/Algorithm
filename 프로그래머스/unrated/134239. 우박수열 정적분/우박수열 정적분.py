def solution(k, ranges):
    answer = []
    temp=[k]
    result = collatz_numbers(k,temp)
    # print(result)
    
    answer=[definite_integral(r[0],r[1], result) for r in ranges]
    
    return answer

def definite_integral(start, end, collatz_nums):
    end_transformed = len(collatz_nums)+end-1
    # print('start:{}, end:{}'.format(start, end))
    # print('start:{}, end_transformed:{}'.format(start, end_transformed))
    if start==0 and end==0:
        start = 0
        end_transformed = len(collatz_nums)-1
    elif start>end_transformed:
        return -1
    elif start == end_transformed:
        return 0
    
    area=0
    for i in range(start, end_transformed, 1):
        area+=0.5*(collatz_nums[i]+collatz_nums[i+1])
    return area

def collatz_numbers(k, result):
    if k==1:
        return result
    elif k%2==0:
        result = collatz_numbers(k/2, result+[k/2])
    else:
        result = collatz_numbers(k*3+1, result+[k*3+1])
        
    return result
    