def solution(storey):
    digits = [int(c) for c in str(storey)]
    answer = recursive_func(digits, 0)
    return answer

def recursive_func(digits, result):
    temp = result
    if len(digits) == 0:
        return result
    else:
        d = 0
        while d == 0 and len(digits)!=0:
            d = digits.pop()

        if d != 0:
            if d < 5:
                temp = recursive_func(digits, temp + d)
            elif d == 5 :
                a = sum(map(lambda x: x>=5, digits))
                b = len(digits)-a
                if a>b and digits[-1]>=5:
                    number = int(''.join([str(c) for c in digits])) + 1
                    digits = [int(i) for i in str(number)]
                    temp = recursive_func(digits, temp + 10 - d)
                else:
                    temp = recursive_func(digits, temp + d)
            else:
                if len(digits)!=0:
                    number = int(''.join([str(c) for c in digits])) + 1
                    digits = [int(i) for i in str(number)]
                    temp = recursive_func(digits, temp + 10 - d)
                else:
                    digits=[1]
                    temp = recursive_func(digits, temp + 10 - d)
    return temp

                
            
    