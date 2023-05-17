from collections import deque
def process_order(priorities, location):
    answer = 0
    queue = deque(priorities)
    
    while True:
        temp = queue.popleft()
        if location > 0 :
            location -= 1
        elif location == 0:
            
        if temp <   
    # p_order = priorities[location]
    # for i in range(len(priorities)):
    #     if (i < location) and priorities[i] >= p_order:
    #         answer += 1
    #     if (i > location) and priorities[i] > p_order:
    #         answer += 1
    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0

print(process_order(priorities, location))