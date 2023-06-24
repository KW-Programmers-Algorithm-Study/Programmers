from heapq import *

def solution(jobs):
    request_time = [tuple(job) for job in jobs]
    heapify(request_time) # 튜플로 넣어 줘야 하는데 
    print(request_time)
    time_cost = []
    next_candidate = []
  
    for i in range(len(request_time)):
        if not time_cost: 
            time_cost.append(heappop(request_time)[1])
            continue
        print(time_cost)
        while request_time and (request_time[0][0] <= time_cost[-1]):
            heappush(next_candidate, heappop(request_time)[1])
            print(next_candidate)
        time_cost.append(heappop(next_candidate) + time_cost[-1])
    
    return sum(time_cost)/len(time_cost)

jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))