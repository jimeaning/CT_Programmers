# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = ''
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    answer = day[(sum(month[:a-1]) + b) % 7]
        
    return answer