# 예산 : https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    sum = 0

    d.sort()

    for i in range(len(d)) :
        if sum + d[i] <= budget :
            answer += 1
            sum += d[i]

    return answer


# 통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.5MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.6MB)
# 테스트 7 〉	통과 (0.05ms, 10.7MB)
# 테스트 8 〉	통과 (0.05ms, 10.7MB)
# 테스트 9 〉	통과 (0.05ms, 10.7MB)
# 테스트 10 〉	통과 (0.05ms, 10.7MB)
# 테스트 11 〉	통과 (0.05ms, 10.7MB)
# 테스트 12 〉	통과 (0.05ms, 10.7MB)
# 테스트 13 〉	통과 (0.05ms, 10.8MB)
# 테스트 14 〉	통과 (0.05ms, 10.7MB)
# 테스트 15 〉	통과 (0.05ms, 10.7MB)
# 테스트 16 〉	통과 (0.06ms, 10.6MB)
# 테스트 17 〉	통과 (0.05ms, 10.7MB)
# 테스트 18 〉	통과 (0.08ms, 10.7MB)
# 테스트 19 〉	통과 (0.05ms, 10.7MB)
# 테스트 20 〉	통과 (0.05ms, 10.7MB)
# 테스트 21 〉	통과 (0.05ms, 10.7MB)
# 테스트 22 〉	통과 (0.05ms, 10.7MB)
# 테스트 23 〉	통과 (0.05ms, 10.7MB)