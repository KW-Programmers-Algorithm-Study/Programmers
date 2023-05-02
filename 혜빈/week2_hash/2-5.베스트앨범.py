def solution(genres, plays):
    answer = [] #노래 장르당 2개씩 넣을 리스트
    played={} #노래당 재생 횟수 넣을 딕셔너리
    genreCnt={} #장르당 재생 횟수 셀 딕셔너리
    
###genres 내 genre당 수 구하기
    for gr in genres:
        # for pl in plays:
        genreCnt[gr]=0
        # print(gr)    
    
    for gernreCntKey in genreCnt.keys(): 
        for gr in genres:
            if gernreCntKey==gr:
                genreCnt[gernreCntKey]+=1 


    glplList=list(zip(genres,plays))
    for i,(gr,pl) in enumerate(glplList):
        print(i,gr,pl)
        played[pl]=gr
    print(played)
    return answer


solution(["classic","pop","classic","classic","pop"],[500, 600, 150, 800, 2500])

#######dummy code
# ###장르 당 플레이 횟수 딕셔너리에 넣기
#     for i in plays:
#         played[i]=1
#     for j in genres:
#         played[i]=j
#     print("played: ",played)    
#     print("genreCnt: ",genreCnt)
### 장르와 pl을 한 배열로 합침
    # glplList=genres+plays
    # print(glplList)    
# ###각 배열의 인덱스 구하기
#     plIdx=[]
#     grIdx=[]
#     for pl in plays:
#         plIdx.append(plays.index(pl))
#     for gr in genres:
#         grIdx.append(genres.index(gr))
# lenGlpl=int(len(glplList)/2)
    # for pl in glplList[lenGlpl:]:
    #     # for gr in glplList[:lenGlpl]: #장르
    #     played[pl]=glplList[:lenGlpl]
    # print(played)