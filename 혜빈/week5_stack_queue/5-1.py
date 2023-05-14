# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

#1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
#2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
#3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

def solution(priorities, location):
    answer = 0
    cnt=0
    for _ in range(len(priorities)):
        prc=priorities.pop(0)
        # print("prc",prc)
        if priorities and prc<priorities[0]: #우선순위 낮으면
            priorities.pop(0)
            cnt+=1
            priorities.insert(0,prc)
            if location==cnt:
                print("cnt: ",cnt)
                answer=cnt
        else: answer=cnt
    print("answer: ",answer)
    return answer

solution([2,1,3,2],2) #1
solution([1,1,9,1,1,1],0) #5