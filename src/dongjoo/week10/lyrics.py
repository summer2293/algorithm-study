# https://programmers.co.kr/learn/courses/30/lessons/60060



# 3rd try:
def is_match(word, pattern):
    if len(word) != len(pattern):
        return False

    # find question mark index
    idx = 0
    if pattern[0] == '?':
        while pattern[idx] == '?':
            idx += 1
        return pattern[idx:] == word[idx:]
    else:
        idx = pattern.index('?')
        return pattern[:idx] == word[:idx]

# 2nd try:
# def is_match(word, pattern):
#     if len(word) != len(pattern):
#         return False
#     for idx in range(len(pattern)):
#         if pattern[idx] == '?':
#             idx += 1
#             continue
#         if pattern[idx] != word[idx]:
#             return False
#     return True

def solution(words, queries):
    answer = []
    count = 0
    for query in queries:
        for word in words:
            if is_match(word, query):
                count += 1
        answer.append(count)
        count = 0
    return answer

print(is_match('frodo', 'fro??'))
print(is_match('frodo', '????o'))



answer = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
                  "fro??", "????o", "fr???", "fro???", "pro?"])
print(answer)


# 1st try:
# 정확성: 25.0
# 효율성: 30.0
# 합계: 55.0 / 100.0

# import re

# def solution(words, queries):
#     patterns = []
#     for query in queries:
#         pattern = re.compile(query.replace('?', '.'))
#         patterns.append(pattern)
    
#     answer = []
#     count = 0
#     for pattern in patterns:
#         for word in words:
#             if len(word) == len(pattern.pattern) and bool(pattern.match(word)):
#                 count += 1
#         answer.append(count)
#         count = 0

#     return answer


# answer = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], [
#                   "fro??", "????o", "fr???", "fro???", "pro?"])
# print(answer)
