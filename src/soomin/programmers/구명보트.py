# programmers lv2 구명보트
# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    answer = 0
    begin, end = 0, len(people)-1
    people.sort()
    while(begin <= end):
        if people[begin] + people[end] <= limit: 
            begin += 1
        end -= 1
        answer += 1
    return answer