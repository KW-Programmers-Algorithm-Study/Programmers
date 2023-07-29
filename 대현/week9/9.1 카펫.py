def addCandidate(num):
    _list = []
    #약수 구하는 함수
    for i in range (int(num ** (1/2))): #int는 내림
        if(num % (i+1) == 0):
            _list.append((i+1, num // (i+1)))                      
    return _list
        
def solution(brown, yellow):
    answer = []
    totalNum = brown + yellow #블럭의 총개수
    candidateList = addCandidate(totalNum) #가로 세로 후보
    for candidate in candidateList:
        if((candidate[0]-2) * (candidate[1]-2) == yellow):
            answer = answer + [candidate[1],candidate[0]]  
    return answer

print(solution(10, 2))