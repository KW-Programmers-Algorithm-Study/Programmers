from sys import stdin, stdout
from collections import Counter
input = stdin.readline

def prefix(phone_book):
    # 문자를 sort 하면 119 ,219, 1191 순이 아닌 119, 1191, 219 순으로 정렬됨!
    # 숫자와 문자열의 정렬의 방향성이 다른것이 point
    phone_book = sorted(phone_book) 
    for i in range(len(phone_book)):
        if i == len(phone_book) - 1:
            break
        prefix = phone_book[i]
        nextWord = phone_book[i+1]
        
        if prefix == nextWord[:len(prefix)]:
            return False
    return True 

phone_book = ["119", "97674223", "1195524421"]
print(phone_book) # 
