# https://programmers.co.kr/learn/courses/30/lessons/12931


def solution(n):
    if n == 0:
        return 0
    return solution(n//10) + n%10

print(solution(987))

# time complexity: log10(n)
# space complexity: log10(n)
