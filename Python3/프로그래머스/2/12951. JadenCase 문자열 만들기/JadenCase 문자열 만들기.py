def solution(s):
    words = s.lower().split(' ') # 공백 문자 연속 가능 

    for i in range(len(words)):
        word = words[i]
        if word != '':
            words[i] = word[0].upper() + word[1:]

    answer = ' '.join(words)
    return answer