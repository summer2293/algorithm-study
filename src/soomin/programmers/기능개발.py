#!/bin/python3
import pytest

@pytest.mark.parametrize("progresses, speeds, expected", [
    ([93,30,55],[1,30,5],[2,1]),
    ([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7], [2,4]),
    ([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7], [1, 2, 3]),
])


def test_simple(progresses, speeds, expected):
    assert solution(progresses, speeds) == expected

COMPLETE = 100
def solution(progresses, speeds):
    answer = []
    complete_days = []
    for i,progress in enumerate(progresses):
        days = (COMPLETE - progress) // speeds[i]
        if (COMPLETE - progress) % speeds[i] > 0: days += 1
        complete_days.append(days)
    
    flag, count = 0, 0
    for i,v in enumerate(complete_days):
        if i == 0:
            flag = complete_days[i]
            continue
        if complete_days[i] <= flag: count += 1
        else:
            answer.append(count+1)
            flag = complete_days[i]
            count = 0
    answer.append(count+1)
    return answer