def solution(s):
    return str(min([int(s) for s in s.split(' ')])) + ' ' + str(max([int(s) for s in s.split(' ')]))