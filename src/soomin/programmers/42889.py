# 실패율 https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    failure = [0] * (N)
    user = len(stages)
    answer = dict()
    for i in stages:
        try: failure[i-1] += 1
        except: pass
    for i,value in enumerate(failure):
        try: answer[i+1] = value/user
        except: answer[i+1] = 0
        user -= value
    return [k for k, v in sorted(answer.items(), key=lambda item: item[1], reverse=True)]

# 테스트 1 〉	통과 (0.04ms, 10.8MB)
# 테스트 2 〉	통과 (0.13ms, 10.8MB)
# 테스트 3 〉	통과 (1.15ms, 15MB)
# 테스트 4 〉	통과 (7.75ms, 81.2MB)
# 테스트 5 〉	통과 (18.23ms, 157MB)
# 테스트 6 〉	통과 (0.16ms, 10.8MB)
# 테스트 7 〉	통과 (0.84ms, 14.5MB)
# 테스트 8 〉	통과 (7.60ms, 81.7MB)
# 테스트 9 〉	통과 (18.19ms, 158MB)
# 테스트 10 〉	통과 (7.52ms, 81.1MB)
# 테스트 11 〉	통과 (7.59ms, 80.5MB)
# 테스트 12 〉	통과 (11.76ms, 118MB)
# 테스트 13 〉	통과 (12.55ms, 125MB)
# 테스트 14 〉	통과 (0.06ms, 10.7MB)
# 테스트 15 〉	통과 (8.74ms, 54.9MB)
# 테스트 16 〉	통과 (2.70ms, 31.1MB)
# 테스트 17 〉	통과 (5.25ms, 54.9MB)
# 테스트 18 〉	통과 (2.64ms, 31.2MB)
# 테스트 19 〉	통과 (0.64ms, 12.2MB)
# 테스트 20 〉	통과 (3.83ms, 42.5MB)
# 테스트 21 〉	통과 (7.64ms, 75.8MB)
# 테스트 22 〉	통과 (18.40ms, 160MB)
# 테스트 23 〉	통과 (16.23ms, 153MB)
# 테스트 24 〉	통과 (15.00ms, 154MB)
# 테스트 25 〉	통과 (0.05ms, 10.6MB)
# 테스트 26 〉	통과 (0.04ms, 10.7MB)
# 테스트 27 〉	통과 (0.04ms, 10.7MB)