def solution(answers):
    answerLength = len(answers)
    answer = []
    soopo1 = [1,2,3,4,5] 
    soopo2 = [2,1,2,3,2,4,2,5]
    soopo3 = [3,3,1,1,2,2,4,4,5,5]
    
    #답안지의 길이에 맞게 각각 수포자들의 정오표를 제작
    soopo1Answer = soopo1 * (answerLength // len(soopo1)) + soopo1[:(answerLength % len(soopo1))]
    soopo2Answer = soopo2 * (answerLength // len(soopo2)) + soopo2[:(answerLength % len(soopo2))]
    soopo3Answer = soopo3 * (answerLength // len(soopo3)) + soopo3[:(answerLength % len(soopo3))]
    
    soopo1Correct=0
    soopo2Correct=0
    soopo3Correct=0
    
    #반복문을 돌면서 채점
    for i in range(answerLength):
        if(answers[i] == soopo1Answer[i]):
            soopo1Correct += 1
        if(answers[i] == soopo2Answer[i]):
            soopo2Correct += 1
        if(answers[i] == soopo3Answer[i]):
            soopo3Correct += 1
    
    #가장 많이 맞춘 애들 정답에 추가
    if(soopo1Correct >= soopo2Correct and soopo1Correct >= soopo3Correct):
        answer.append(1)
    if(soopo2Correct >= soopo1Correct and soopo2Correct >= soopo3Correct):
        answer.append(2)
    if(soopo3Correct >= soopo1Correct and soopo3Correct >= soopo2Correct):
        answer.append(3)
        
    return answer


print(solution([1,2,3,4,5]))