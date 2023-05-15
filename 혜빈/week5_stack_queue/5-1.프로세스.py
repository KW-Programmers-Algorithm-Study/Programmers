# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

#1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
#2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
#3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

# 배열 내 최대 값을 구한다 => 최대값과 각 프로세스를 비교한다. => 최대값이 첫번째라면, 다른 배열에 넣고, 원래 배열에서 삭제, cnt+1 => 다시 최대값 구해서 비교 
# 최대값이 첫번째가 아니라면, 삭제 후 배열의 맨뒤로 다시 보냄 , 삭제시마다 cnt + 1  
def solution(priorities, location):
    answer = 0
    cnt=0
    q=[]
    loc=priorities[location]

    while priorities:
        mx=max(priorities)
        if mx ==priorities[0]:
            q.append(priorities.pop(0))
            cnt+=1
            if loc in q:
                break
            # answer=q.index(loc)
        elif mx<priorities[0]:
            priorities.append(priorities.pop(0))
            cnt+=1
            if loc in q:
                break
            answer=cnt
        elif mx>priorities[0]:
            priorities.append(priorities.pop(0))
            cnt+=1
            answer=cnt
    answer=q.index(loc)+1 #같은 수가 여러개 있다면?
        
    # print("cnt",cnt)
    print("prior",priorities)
    print("q: ",q)
    print("answer: ",answer)
    return answer

solution([3,1,4,2],2) #1
solution([3,1,4,2],1) #4
solution([1,1,9,1,1,1],0) #5