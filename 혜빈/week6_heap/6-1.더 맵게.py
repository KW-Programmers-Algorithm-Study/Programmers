import heapq as hq

import heapq as hq

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    #남은 요소가 2개부터일 때
    while len(scoville)>1: #IndexError & h2까지 구해야 하므로
        h1=hq.heappop(scoville) #첫번째로 작은 요소
        
        if h1> K:
            # break로 했을 땐 효율성 테스트 통과 x + 정답률 더 낮
            print(answer)
            return answer
        
        else:
            h2=hq.heappop(scoville) #두번째로 작은 요소
            hq.heappush(scoville,h1+h2*2)
            answer+=1
    #남은 요소가 1개이고 K보다 작을 때
    if hq.heappop(scoville) < K:
        answer=-1
        print(answer)
        print(scoville)
        return answer
    

solution([1,2,3,9,10,12],7) #2