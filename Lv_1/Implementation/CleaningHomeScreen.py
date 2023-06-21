# 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = []
    x = []
    y = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                x.append(i)
                y.append(j)
                
    answer.append(min(x))
    answer.append(min(y))
    answer.append(max(x)+1)
    answer.append(max(y)+1)
            
    return answer