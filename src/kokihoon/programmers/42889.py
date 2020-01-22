# 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889

import operator

def solution(N, stages):
    length = len(stages)
    answer = []
    sum = 0
    stages.sort()
    j = 1
    k = 0

    while k < len(stages) :
        if stages[k] == j :
            sum +=1
            k += 1
        else :
            answer.append(sum/length)
            length -= sum
            sum = 0
            j += 1

    answer.append(sum/length)
    answer = answer[0:N]
    answer1 = []
    for idx, val in enumerate(answer):
        answer1.append((idx+1, val))

    answer2 = sorted(answer1, key=operator.itemgetter(1), reverse=True)
    answer3 = []
    for (i, d) in answer2 :
        answer3.append(i)

    return answer3

    
# 테스트 1 〉	실패 (0.39ms, 10.8MB)
# 테스트 2 〉	통과 (0.26ms, 10.8MB)
# 테스트 3 〉	통과 (2.99ms, 15.1MB)
# 테스트 4 〉	통과 (24.91ms, 81.3MB)
# 테스트 5 〉	통과 (52.70ms, 156MB)
# 테스트 6 〉	실패 (0.99ms, 10.9MB)
# 테스트 7 〉	실패 (3.22ms, 14.6MB)
# 테스트 8 〉	통과 (25.45ms, 81.6MB)
# 테스트 9 〉	실패 (53.46ms, 157MB)
# 테스트 10 〉	통과 (23.89ms, 81.4MB)
# 테스트 11 〉	통과 (24.05ms, 82MB)
# 테스트 12 〉	통과 (36.10ms, 116MB)
# 테스트 13 〉	실패 (41.01ms, 125MB)
# 테스트 14 〉	통과 (0.06ms, 10.8MB)
# 테스트 15 〉	통과 (12.98ms, 54.9MB)
# 테스트 16 〉	통과 (6.86ms, 31.2MB)
# 테스트 17 〉	통과 (12.90ms, 54.8MB)
# 테스트 18 〉	통과 (6.90ms, 31.3MB)
# 테스트 19 〉	통과 (1.46ms, 12.2MB)
# 테스트 20 〉	통과 (10.15ms, 42.4MB)
# 테스트 21 〉	통과 (19.57ms, 76.1MB)
# 테스트 22 〉	통과 (30.39ms, 159MB)
# 테스트 23 〉	실패 (37.34ms, 152MB)
# 테스트 24 〉	실패 (44.11ms, 154MB)
# 테스트 25 〉	실패 (0.25ms, 10.8MB)
# 테스트 26 〉	통과 (0.04ms, 10.8MB)
# 테스트 27 〉	통과 (0.04ms, 10.7MB)