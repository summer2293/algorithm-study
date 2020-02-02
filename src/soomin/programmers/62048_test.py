import pytest
import collections
import re


@pytest.mark.parametrize("w,h, expected", [
    (8, 12, 80)
])


def test_simple(w,h, expected):
    assert solution(w,h) == expected


def solution(w,h):
    answer = 0
    short, long = min(w,h), max(w,h)
    while (short != 0):
        if short == 1:
            answer += 0 
            break
        count, long = long//short, long%short
        answer += (short * short - short) * count
        short, long = min(short,long), max(short,long)
    return answer

if __name__ == "__main__":
    solution(w, h)
    