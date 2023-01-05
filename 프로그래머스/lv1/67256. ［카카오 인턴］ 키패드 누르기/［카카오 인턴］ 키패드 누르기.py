def solution(numbers, hand):
    answer = ''
    # keypad = [[1,2,3], 
    #           [4,5,6], 
    #           [7,8,9], 
    #           [-1,0,-1]]
    number_position = [[3, 1], 
                       [0, 0], [0, 1], [0, 2], 
                       [1, 0], [1, 1], [1, 2], 
                       [2, 0], [2, 1], [2, 2]]
    
    left_hand_position = [3, 0]
    right_hand_position = [3, 2]   
    
    for n in numbers:
        
        target_position = number_position[n]
        
        if n==2 or n==5 or n==8 or n==0:
            dis_left = manhatan_distance(left_hand_position, target_position)
            dis_right = manhatan_distance(right_hand_position, target_position)

            if dis_left>dis_right:
                right_hand_position=target_position
                answer = answer + "R"
            elif dis_left<dis_right:
                left_hand_position=target_position
                answer = answer + "L"
            else:
                if hand=="left":
                    left_hand_position=target_position
                    answer = answer + "L"
                elif hand=="right":
                    right_hand_position=target_position
                    answer = answer + "R"
                else:
                    pass
                
        elif n==1 or n==4 or n==7:
            left_hand_position=target_position
            answer = answer + "L"
        else:
            right_hand_position=target_position
            answer = answer + "R"
            
    return answer

def manhatan_distance(departure, destination):
    distance=0
    distance = abs(departure[0]-destination[0]) + abs(departure[1]-destination[1])
    return distance