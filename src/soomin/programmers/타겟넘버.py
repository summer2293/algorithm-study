# programmers lv2 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
# 별로인 내코드
from itertools import permutations, combinations
def solution(numbers, target):

    idx = []
    answer = 0
    for i in range(len(numbers)):
        idx.append(i)

    sumdata = sum(numbers)
    for i in range(len(numbers)+1):
        combination = [list(number) for number in combinations(idx, i)]
        for minuslist in combination:
            minusdata = 0
            for number in minuslist:
                minusdata += numbers[number] 
            if (sumdata - (minusdata * 2)) == target:
                answer += 1
    return answer


# 개쩌는 코드

def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0]) 