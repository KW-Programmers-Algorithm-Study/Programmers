def solution(clothes):
    answer=0
    closet={}
    
    for i in range(len(clothes)):
        cloth=clothes[i][0]
        clothType=clothes[i][1]
        closet[cloth]=clothType
    print("closet: ",closet)
    #  {'yellow_hat': 'headgear', 'blue_sunglasses': 'eyewear', 'green_turban': 'headgear'}
    #  {'crow_mask': 'face', 'blue_sunglasses': 'face', 'smoky_makeup': 'face'}
    
    
    # for i in range(len(closet)):
    #     answer+=i
        # for v in closet.values():
        #     print(v)
        #     if v[i]==v[i+2]:
        #         answer+=1
        # for j in range(len(closet)):
        #     if closet.values[i]==closet.values[i+j]:
        #         answer=len(closet)+
    hashList=[]
    for i in closet.values():
        hsValue=hash(i)
        hashList.append(hsValue)
    print(hashList)
    
    # value의 해시값이 같다면
    if len(hashList)!=len(set(hashList)) and len(set(hashList))==1:
        answer=len(hashList)
    elif len(hashList)!=len(set(hashList)):
        answer=len(hashList)+len(set(hashList))
    else:
        answer=len(hashList)  
  
    print(answer)
    return answer


solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])