def solution(s):
    # 1.괄호의 총 개수가 짝수여야 함
    # 2.(와 )의 개수가 같아야 함
    # 3.처음은 (, 마지막은 )여야 함
    answer = True
    left=0
    right=0
    if len(s)%2==1 or s[0]!="(": #홀수 개수 혹은 "("로 시작하지 않으면
        answer=False
    elif len(s)%2==0 and s[0]=="(" : #짝수 개수고, "("로 시작할 때 
        for ss in s:
            if ss=="(": #(이 나오면
                left+=1 # +1
            elif ss==")": #)이 나오면
                left-=1  #+1
                s.pop(ss)
        # print("left: ",left, "right: ",right)                   
        if left==0 and s[-1]==")": #(과 )의 개수가 같고, 마지막이 )라면
            answer=True
        else: answer=False
    print(answer)
    return answer

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")
solution("())(()") #issue 
