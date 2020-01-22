# 모의고사 : https://programmers.co.kr/learn/courses/30/lessons/42840

from itertools import cycle

def solution(answers):
    answer = []
    count = [0,0,0]
    player_1 = [1,2,3,4,5]
    player_2 = [2,1,2,3,2,4,2,5]
    player_3 = [3,3,1,1,2,2,4,4,5,5]

    for p1, p2, p3, answer in zip(cycle(player_1), cycle(player_2), cycle(player_3), answers) :
        if p1 == answer :
            count[0] += 1
        if p2 == answer :
            count[1] += 1
        if p3 == answer :
            count[2] += 1

    max_num = max(count)

    for i in range(len(count)) :
        if count[i] == max_num :
            answer.append(i+1)

    return answer


    