import itertools

def solution(k, dungeons):
    #주어진 던전들로 만들 수 있는 모든 순서를 순열로 찾음
    nPr = list(itertools.permutations(dungeons, len(dungeons)))
    #정답으로 반환할 값
    maxNum = 0
    for i in nPr:
        #모든 순열을 돌면서 클리어한 던전 개수를 측정
        num = 0
        flag = k
        for j in list(i):
            if flag >= j[0]:
                num = num + 1
                flag=flag-j[1]
            else:
                pass
        #기존 최대치보다 크면 업데이트 해주기
        if num > maxNum:
            maxNum = num          
    return maxNum

print(solution(80,[[80,20],[50,40],[30,10]]))