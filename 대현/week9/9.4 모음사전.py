def solution(word):
    answer = 0
    #1+5+5^2+5^3+5^4, 1+5+5^2+5^3, 1+5+5^2, 1+5, 1
    index = [781, 156, 31, 6, 1]
    wordList = list(word)
    for i in range(len(wordList)):
        if(wordList[i] == 'A'):
            answer = answer + 1 + index[i] * 0
        elif(wordList[i] == 'E'):
            answer = answer + 1 + index[i] * 1
        elif(wordList[i] == 'I'):
            answer = answer + 1 + index[i] * 2
        elif(wordList[i] == 'O'):
            answer = answer + 1 + index[i] * 3
        elif(wordList[i] == 'U'):
            answer = answer + 1 + index[i] * 4
    return answer

print(solution("EIO"))