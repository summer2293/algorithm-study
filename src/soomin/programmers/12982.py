# 예산 https://programmers.co.kr/learn/courses/30/lessons/12982
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break;
        answer += 1
    return answer

# 테스트 1 〉	통과 (0.03ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.7MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.05ms, 10.7MB)
# 테스트 9 〉	통과 (0.05ms, 10.9MB)
# 테스트 10 〉	통과 (0.04ms, 10.8MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.07ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.8MB)
# 테스트 14 〉	통과 (0.05ms, 10.6MB)
# 테스트 15 〉	통과 (0.05ms, 10.7MB)
# 테스트 16 〉	통과 (0.05ms, 10.8MB)
# 테스트 17 〉	통과 (0.06ms, 10.8MB)
# 테스트 18 〉	통과 (0.05ms, 10.8MB)
# 테스트 19 〉	통과 (0.05ms, 10.8MB)
# 테스트 20 〉	통과 (0.04ms, 10.8MB)
# 테스트 21 〉	통과 (0.04ms, 10.7MB)
# 테스트 22 〉	통과 (0.04ms, 10.8MB)
# 테스트 23 〉	통과 (0.04ms, 10.8MB)