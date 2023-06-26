import heapq as hq

def solution(o):
    answer=[]
    
    for i in o:
        a,num=i.split()
        num=int(num)

        if a =="I": # 배열에 값 삽입
            hq.heappush(answer,num)
        elif a=="D" and num==1: #최대값 삭제
            if len(answer)!=0:
                maxV=max(answer)
                answer.remove(maxV)
        elif a=="D" and num==-1: #최소값 삭제
            if len(answer)!=0:
                hq.heappop(answer)

    #모든 연산 처리 후 
    if len(answer)==0:
     #큐 비어있으면      
        answer=[0,0]
    # 큐가 비어있지 않으면
    else:
        answer=[max(answer),hq.heappop(answer)]

    print(answer)
    return(answer)

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])