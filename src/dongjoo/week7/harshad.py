# https://programmers.co.kr/learn/courses/30/lessons/12947


def solution(x):
    return 0 == x % sum([int(s) for s in str(x)])


# 숏코딩 
# time complexity: linear , str(x)가 list comprehension 시 한번만 수행되낭..? 설마 매번 되지 않겠지?
# time complexity: log10(x)
print(solution(12))