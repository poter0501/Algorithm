def solution(elements):
    answer = 0
    l=len(elements)
    sum_of_subs=set()
    sum_of_subs.add(sum(elements))
    elements=elements+elements
    
    
    for start in range(0, l):
        for sub_l in range(1, l):
            sum_of_subs.add(sum(elements[start:start+sub_l]))
                          
    return len(sum_of_subs)