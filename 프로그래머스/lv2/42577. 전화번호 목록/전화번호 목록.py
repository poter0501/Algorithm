def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x: -len(x))
    tree = {}
    idx = 0
    for number in phone_book:
        partial_tree = tree
        result = False
        for i, n in enumerate(number):
            if n not in partial_tree:
                partial_tree[n] = {}
            else:
                if len(number) == i+1:
                    return False
            partial_tree = partial_tree[n]
        if idx == 0:
            answer = True
        idx+=1
    return answer