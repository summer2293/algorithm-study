# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter
def solution(participant, completion):
    return [i for i in (Counter(participant) - Counter(completion)).keys()][0]

# 숏코딩
# time & space complexity: n + m


# print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
# print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
#                ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'],['stanko', 'ana', 'mislav']))
