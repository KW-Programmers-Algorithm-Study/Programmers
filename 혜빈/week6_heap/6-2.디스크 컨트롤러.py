# 반환값 정수
# 두번째 인자 오름차순으로 리스트 정렬
# 
import heapq as hq

def solution(jobs):
    answer = 0
    odr=[] #order 

    # 두번째 인자 오름차순으로 리스트 정렬
    for i,j in jobs:
        odr.append(j)
    odr.sort()
    

    # hq.heapify(odr)
    print(odr)
    print(answer)
    return answer

solution([[0, 3], [1, 9], [2, 6]]) #9
