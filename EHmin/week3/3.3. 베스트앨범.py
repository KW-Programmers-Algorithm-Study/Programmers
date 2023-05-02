from sys import stdin, stdout
from collections import Counter
input = stdin.readline

def best_Album(genres, plays):
    answer = []
    dict = {}
    for i in range(len(genres)):
        if genres[i] not in dict:
            dict[genres[i]] = [i]
        else:
            dict[genres[i]] = dict.get(genres[i]) + [i] 
            # dict[genres[i]] = dict.get(genres[i]).append(plays[i]) 위랑 동일한 동작이락 생각하는데 왜 error가 발생하는지 모르겠음
    # sorted_dict = sorted(dict.items(), key = lambda x : len(x[1]) , reverse= True)
    sorted_dict = sorted(dict.items(), key = lambda x : sum(plays[i] for i in x[1]) , reverse= True)
    
    for tuple in sorted_dict:
        sorted_list = sorted(tuple[1] , key= lambda x : plays[x], reverse=True)
        answer = answer + sorted_list[0:2]
    return answer
    
        
    
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# genres = ["pop", "classic", "classic", "classic", "pop"]
# plays = [600, 500, 150, 800, 2500]

print(best_Album(genres, plays))