n = int(input())
k = int(input())
cards = []
for i in range(n):
    cards.append(int(input()))


def combination_recursive(input_cards, num):
    result = []
    if num == 1:
        result = [[c] for c in input_cards]
        return result
    else:
        for i in range(len(input_cards)):
            if i == 0:
                result = result + [c + [input_cards[i]] for c in combination_recursive(input_cards[i + 1:], num - 1)]
            elif i == len(input_cards) - 1:
                result = result + [c + [input_cards[i]] for c in combination_recursive(input_cards[:i], num - 1)]
            else:
                result = result + [c + [input_cards[i]] for c in
                                   combination_recursive(input_cards[:i] + input_cards[i + 1:], num - 1)]

        return result


combinations = combination_recursive(cards, k)
# print(combinations)
result = set()
for combi in combinations:
    temp = ''
    for i in range(k):
        temp = temp + str(combi[i])
    result.add(temp)
# print(result)
print(len(result))
