from heapq import *

def solution(operations):
    is_max = False
    heap = []
    answer = [0,0]
    for operation in operations:
        operator, value = operation.split()
        if operator == 'I':
            if is_max:
                heappush(heap,-int(value))
            else:
                heappush(heap,int(value))
        elif operator == 'D':
            if not heap:
                continue
            if value == '1':
                if is_max:
                    heapify(heap)
                    heappop(heap)
                else:
                    heap = [ -1 * i for i in heap]
                    heapify(heap)
                    is_max = True
                    heappop(heap)
            elif value == '-1':
                if is_max:
                    heap = [ -1 * i for i in heap]
                    heapify(heap)
                    is_max = False
                    heappop(heap)
                else:
                    heappop(heap)
                    
    if heap:
        answer.clear()
        if is_max:
            heap = [ -1 * i for i in heap]
            heap = sorted(heap)
        else:
            heap = sorted(heap)
        answer = [heap[-1], heap[0]]

    return answer
        

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))