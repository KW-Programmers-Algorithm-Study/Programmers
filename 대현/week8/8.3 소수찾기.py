import itertools

def is_prime(x):    #소수 판별 함수
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    n = list(numbers)
    nList = [] #주어진 수를 가지고 순열로 만들 수 있는 모든 조합
    for i in range(len(n)):
        nList += (list(itertools.permutations(n,i+1)))
    nums = []
    # print(nList)
    for j in nList:
        num = ''
        for h in j:
            num += h
        #0과 1은 소수가 아님
        if(int(num) == 0 or int(num) == 1):
            pass
        else:
            nums.append(int(num))
    #중복을 제거해주기
    answerList = list(set(nums))
    # print(answerList)
    #소수면 숫자 늘려주기
    for ans in answerList:
        if is_prime(ans):
            answer += 1
    return answer

print(solution("17"))