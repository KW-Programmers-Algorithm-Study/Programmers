from heapq import *

def solution(jobs):
    request_time = [tuple(job) for job in jobs]
    heapify(request_time)
    current_time = request_time[0][0]
    next_candidate = []
    heapify(next_candidate)
    time_cost = []
    nothing_todo = True
  
    while request_time or next_candidate :
        # print()
        while request_time and (request_time[0][0] <= current_time):
            item_r = heappop(request_time)
            heappush(next_candidate, (item_r[1], item_r[0]))
            nothing_todo = False
            
        # print(next_candidate)
        
        if nothing_todo:
            current_time = request_time[0][0]
        else:
            item_n = heappop(next_candidate)
            current_time += item_n[0]
            time_cost.append(current_time - item_n[1])
            if not next_candidate:
                nothing_todo = True
            # print(current_time)
            # print(time_cost)
        
        
    return int(sum(time_cost)/len(time_cost))

jobs = [[0, 10], [0, 1], [0, 1]]

print(solution(jobs))