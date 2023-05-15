# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

#1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
#2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
#3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#   3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.

def solution(priorities, location):
    answer = 0
    q=[] #중요도 순서대로 담을 큐
    # loc=priorities[location]
        
    while priorities: # 우선순위 리스트가 빌 때까지
        mx=max(priorities) #최대값 
        if location==0: #1. location이 0일 때
            if mx>priorities[0]: #최대값이 중요도 배열의 첫번째 순서보다 크다면
                priorities.append(priorities.pop(0)) #삭제 후 뒤로 보내서 추가함
                location=len(priorities)-1 #맨 뒤로 보냈으므로 location 재설정
            else: #최대값이 중요도 배열의 첫번째 순서와 같다면
                q.append(priorities.pop(0)) #최대 중요도 삭제 후 추가
                answer+=1 #순서 +1(0부터 시작하므로)
                break #반복문 탈출
        else: #location이 0이 아니라면(순서가 궁금한 요소가 뒤에 있다면)
            if mx>priorities[0]: #최대값이 첫번째 요소보다 클 때
                priorities.append(priorities.pop(0)) #첫번째 요소를 뒤로 보냄
                location-=1 #앞으로 하나씩 당겨지기 때문에 -1
            else:  #최대값이 첫번째 요소와 같을 때
                q.append(priorities.pop(0)) #q 배열에 추가하고
                location-=1 #앞에서 한개씩 당겨지므로
                answer+=1 #순서 +1
                 
    # print("q: ",q)
    # print("answer: ",answer)
    return answer

solution([3,1,4,2],2) #1 
solution([3,1,4,2],3) #3 1423 4231 231 312 12 21 1 q:4321 
solution([1,1,9,1,1,1],0) #5