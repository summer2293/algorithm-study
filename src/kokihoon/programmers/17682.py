

import re

def solution(dartResult):

    answer = 0
    result = []

    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)

    for index, score in enumerate(scores):
        num = int(score[0])
        bouns = score[1]
        option = score[2]

        if bouns == 'S' :
            bouns = 1
        elif bouns == 'D' :
            bouns = 2
        elif bouns == 'T' :
            bouns = 3

        if option == '*' :
            if index == 0 :
                result.append(num**bouns*2)
            else :
                result[index-1] *= 2
                result.append(num**bouns*2)
        elif option == '#' :
            result.append(num**bouns*-1)
        else :
            result.append(num**bouns)
    answer = sum(result)

    return answer


# 테스트 1 〉	통과 (0.21ms, 10.7MB)
# 테스트 2 〉	통과 (0.20ms, 10.8MB)
# 테스트 3 〉	통과 (0.20ms, 10.8MB)
# 테스트 4 〉	통과 (0.21ms, 10.8MB)
# 테스트 5 〉	통과 (0.21ms, 10.9MB)
# 테스트 6 〉	통과 (0.21ms, 10.8MB)
# 테스트 7 〉	통과 (0.21ms, 10.8MB)
# 테스트 8 〉	통과 (0.21ms, 10.9MB)
# 테스트 9 〉	통과 (0.23ms, 10.8MB)
# 테스트 10 〉	통과 (0.21ms, 10.9MB)
# 테스트 11 〉	통과 (0.21ms, 10.9MB)
# 테스트 12 〉	통과 (0.21ms, 10.8MB)
# 테스트 13 〉	통과 (0.21ms, 10.7MB)
# 테스트 14 〉	통과 (0.20ms, 10.8MB)
# 테스트 15 〉	통과 (0.20ms, 10.9MB)
# 테스트 16 〉	통과 (0.21ms, 10.8MB)
# 테스트 17 〉	통과 (0.21ms, 10.8MB)
# 테스트 18 〉	통과 (0.21ms, 10.8MB)
# 테스트 19 〉	통과 (0.20ms, 10.8MB)
# 테스트 20 〉	통과 (0.20ms, 10.9MB)
# 테스트 21 〉	통과 (0.21ms, 10.8MB)
# 테스트 22 〉	통과 (0.21ms, 10.8MB)
# 테스트 23 〉	통과 (0.22ms, 10.7MB)
# 테스트 24 〉	통과 (0.22ms, 10.8MB)
# 테스트 25 〉	통과 (0.21ms, 10.9MB)
# 테스트 26 〉	통과 (0.21ms, 10.7MB)
# 테스트 27 〉	통과 (0.20ms, 10.9MB)
# 테스트 28 〉	통과 (0.21ms, 10.8MB)
# 테스트 29 〉	통과 (0.21ms, 10.7MB)
# 테스트 30 〉	통과 (0.21ms, 10.8MB)
# 테스트 31 〉	통과 (0.20ms, 10.8MB)
# 테스트 32 〉	통과 (0.21ms, 10.8MB)