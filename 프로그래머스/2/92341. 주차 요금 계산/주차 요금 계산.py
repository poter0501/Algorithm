import math

def solution(fees, records):
    answer = []
    default_time, default_fee, unit_time, unit_fee=fees
    
    accumulated_time={}
    parking_lots={}
    for record in records:
        time, car_num, action = record.split(' ')
        if action=='IN':
            parking_lots[car_num]=minutes(time)
        else:
            in_time = parking_lots.pop(car_num)
            if car_num in accumulated_time:
                accumulated_time[car_num]+=minutes(time)-in_time
            else:
                accumulated_time[car_num]=minutes(time)-in_time
                
    for k in parking_lots:
        in_time = parking_lots[k]
        if k in accumulated_time:
            accumulated_time[k]+=minutes('23:59')-in_time
        else:
            accumulated_time[k]=minutes('23:59')-in_time
    
    for car_num in sorted(accumulated_time):
        t = accumulated_time[car_num]
        if t<=default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee+(math.ceil((t-default_time)/unit_time))*unit_fee)
    return answer

def minutes(time):
    total=time.split(':')
    h, m = int(total[0]), int(total[1])
    return h*60+m

    