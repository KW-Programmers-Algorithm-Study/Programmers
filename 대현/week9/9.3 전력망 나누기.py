from collections import deque 

def solution(n, wires):
    answer = []
    #엣지를 모두 돌면서 확인, 엣지의 개수는 노드-1
    for i in range(n-1):
        leftTree = [wires[i][0]]
        rightTree = [wires[i][1]]
        deq = wires.copy()
        deq.remove(wires[i])
        deq = deque(deq)    
        while(deq):
            wire = deq.popleft()
            if(wire[0] in leftTree or wire[1] in leftTree):
                leftTree = leftTree + wire
            elif(wire[0] in rightTree or wire[1] in rightTree):
                rightTree = rightTree + wire
            else:
                #어디에도 포함이 안되면 다시 뒤로 넣어주기
                deq.append(wire)
        #두 트리간의 차이를 추가    
        answer.append(abs(len(set(leftTree))-len(set(rightTree))))
    return min(answer)

print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))