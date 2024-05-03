def solution(n, words):
    answer=[0,0]
    recorded_words=set()
    prev_word=''
    for i, word in enumerate(words):
        if word in recorded_words:
            return [(i%n)+1, (i//n)+1]
        elif prev_word and prev_word[-1]!=word[0]:
            return [(i%n)+1, (i//n)+1]
        else:
            prev_word=word
            recorded_words.add(word)
    return answer