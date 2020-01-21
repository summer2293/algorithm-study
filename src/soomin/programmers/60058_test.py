import pytest
import collections
import re


@pytest.mark.parametrize("p, expected", [
    ("(()())()", "(()())()"),
    (")(", "()"),
    ("()))((()", "()(())()"),
    ("", ""),
])


def test_simple(p, expected):
    assert solution(p) == expected


def solution(p):
    # 1. 빈문자 or 올바른 문자 check()
    if correct(p) is True: return p # 1, 2입력이 빈 문자열, 완전 문자열 반환 
    # 2. u, v 분리 
    idx = balance(p) + 1
    u, v = p[:idx],  p[idx:]
    #3. 문자열 u가 "올바른 괄호 문자열"  
    if correct(u): return u + solution(v)
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 
    else: return "(" + solution(v) + ")" + swap(list(u)[1:-1]) 

# left, right 변수 1개로 변경 
def correct(p):
    count = 0 
    for char in p:
        if char == "(": count += 1
        else: count -= 1
        if count < 0: return False
    return True


def balance(p):
    count = 0
    for idx, char in enumerate(p):
        count = count-1 if char == "(" else count+ 1
        if count == 0: return idx

def swap(u):
    answer = ''
    for char in u:
        if char == "(": answer += ")"
        else: answer += "("
    return answer


if __name__ == "__main__":
    solution(p)
    