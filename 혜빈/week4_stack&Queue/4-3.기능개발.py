from collections import deque #popleft(). 큐: LIFO

def solution(progresses, speeds):
    answer = [] #여기에 작업 완료되는 순서대로 각 배열에서 빼서 넣기(popleft 사용)
    cpltDay=deque([]) #작업완료에 걸리는 시간 순서대로 넣기
    # cpltDay=queue.PriorityQueue()#작업완료에 걸리는 시간 순서대로 넣기
    # rmdList=[] #나머지를 넣을 배열
    
###작업 완료에 걸리는 시간 계산하기
    for prg,spd in (zip(progresses,speeds)): #모든 스피드로 프로그레스를 나누는 것이 아닌 각 인덱스마다 한번씩만 나눠야 하므로 zip 사용
        cplt=(100-prg)//spd
        rmd=(100-prg)%spd
        # rmdList.append(rmd)
        if rmd!=0 and rmd<spd: #스피드를 각자 프로그레스에 더했을 때 100이 안 되면 작업을 하루 더하므로 1을 더함
            cplt+=1
        cpltDay.append(cplt)    
        # print(prg,spd)
        # print(cplt)
    print("cpltDay",cpltDay)
    # print(rmdList)
    
###각 날짜마다 배포되는 기능 개수 구하기 
## => 기능은 프로그레스의 앞 순서부터 배포되어야 함. 뒷순서는 완성이어도 앞 안되면 배포 x. 앞에서부터 빼기
    # for i in range(len(cpltDay)):
    #     print(cpltDay.popleft())
    import itertools
    for cplt1, cplt2 in zip(cpltDay,itertools.islice(cpltDay,1,len(cpltDay))):
        if cplt1<cplt2:
            # cpltDay.popleft()
            print(cpltDay)


    return answer
solution([93,30,55],[1,30,5]) #7일, 3일, 9일 후 완료, (100-prg)%spd 에서 0이면 완료, !0이면 +1: [2,1]
solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1])# 5,10,1,1,20,1일 후 완료: [1,3,2]