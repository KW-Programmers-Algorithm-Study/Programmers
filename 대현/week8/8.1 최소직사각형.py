def solution(sizes):
    #직사각형엔 두변이 존재
    #기존에 주어진 가로 세로를 사용하지 않고 새로 정의
    #길이가 긴 쪽을 가로, 길이가 짧은 쪽을 세로
    widthList = []
    lengthList = []
    for size in sizes:
        if(size[0]>=size[1]): 
            widthList.append(size[0])
            lengthList.append(size[1])
        else:
            widthList.append(size[1])
            lengthList.append(size[0])
            
    #가로 길이 중 가장 긴 곳과 세로 길이 중 가장 긴 값을 곱하여 반환
    return(max(widthList) * max(lengthList))

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))