# programmers lv2 쇠막대기
# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution(arrangement):
    answer = 0
    stick = []
    for idx, value in enumerate(arrangement): # O(N)
        if value == "(": 
            stick.append(idx)
        if stick and value == ")":
            right, left = idx, stick.pop()
            if right - left == 1: 
                answer += len(stick)
            else: 
                answer += 1
    return answer