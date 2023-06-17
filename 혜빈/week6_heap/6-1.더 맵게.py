import heapq as hq

def solution(scoville, K):
    answer = 0
    for i in scoville:
        while i > K:
            h1=hq.heappop(scoville) #첫번째로 작은 요소
            h2=hq.heappop(scoville) #두번째로 작은 요소
            hq.heappush(scoville, h1+h2*2)
            answer+=1
    print(answer)
    print(scoville)
    return answer

solution([1,2,3,9,10,12],7) #2