# 완주하지 못한 선수 : https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion) :
        if par != com :
            return par

    return participant[-1]

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.25ms, 11MB)
# 테스트 4 〉	통과 (0.47ms, 11.1MB)
# 테스트 5 〉	통과 (0.50ms, 11MB)
# 효율성  테스트
# 테스트 1 〉	통과 (38.65ms, 86.6MB)
# 테스트 2 〉	통과 (66.71ms, 127MB)
# 테스트 3 〉	통과 (90.43ms, 155MB)
# 테스트 4 〉	통과 (88.68ms, 167MB)
# 테스트 5 〉	통과 (93.56ms, 167MB)