def solution(genres, plays):
    answer = []
    dict_album = {}
    for i, gen in enumerate(genres):
        if gen in dict_album:
            dict_album[gen][0] += plays[i]
            if len(dict_album[gen][1]) < 2:
                dict_album[gen][1].append([i, plays[i]])
                dict_album[gen][1].sort(key = lambda x: (-x[1], x[0]))
            else:
                temp = dict_album[gen][1]
                temp.append([i, plays[i]])
                temp.sort(key = lambda x: (-x[1], x[0]))
                dict_album[gen][1] = temp[:2]
        else:
            dict_album[gen] = [plays[i], [[i, plays[i]]]]
        
    midterm = [dict_album[key] for key in dict_album]
    midterm.sort(key = lambda x: -x[0])
    for play_num, song_info in midterm:
        for num, play in song_info:
            answer.append(num)
    
    return answer