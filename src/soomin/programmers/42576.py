# 완주하지 못한 선수  https://programmers.co.kr/learn/courses/30/lessons/42576
import collections 
# collection 끼리는 가감이 가능 
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 테스트 1 〉	통과 (0.20ms, 10.7MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.23ms, 10.9MB)
# 테스트 4 〉	통과 (0.40ms, 11.1MB)
# 테스트 5 〉	통과 (0.43ms, 11.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (26.02ms, 87.3MB)
# 테스트 2 〉	통과 (42.64ms, 127MB)
# 테스트 3 〉	통과 (44.80ms, 154MB)
# 테스트 4 〉	통과 (64.97ms, 169MB)
# 테스트 5 〉	통과 (66.30ms, 167MB)

# # 이전 코드
# def solution(participant, completion):
#     challenger = {}
    
#     for man in participant:
#         try: challenger[man] += 1
#         except: challenger[man] = 1
    
#     for man in completion:
#         challenger[man] -= 1
#         if challenger[man] == 0:
#             del challenger[man]
    
#     for i in challenger:
#         return i 