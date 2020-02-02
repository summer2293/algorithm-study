# programmers lv2 Jendercase
# https://programmers.co.kr/learn/courses/30/lessons/12951
# 별로인 내코드
import pytest
import collections
import re


@pytest.mark.parametrize("s, expected", [
    ("3people unFollowed me", "3people Unfollowed Me"),
    ("for the last week", "For The Last Week"),
    ("hello  new  world", "Hello  New  World"),
])


def test_simple(s, expected):
    assert solution(s) == expected


def solution(s):
    answer = ''
    flag = True
    for char in s:
        if char == " ":
            answer += char.lower()
            flag = True
        else:
            if flag:
                flag = False
                answer += char.upper()
            else:
                answer += char.lower()
    return answer

if __name__ == "__main__":
    solution(s)
    