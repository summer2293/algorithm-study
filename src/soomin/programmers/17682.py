# 다트게임 
# 테스트 1 〉	통과 (0.29ms, 10.8MB)
# 테스트 2 〉	통과 (0.29ms, 11MB)
# 테스트 3 〉	통과 (0.27ms, 10.9MB)
# 테스트 4 〉	통과 (0.32ms, 11MB)
# 테스트 5 〉	통과 (0.29ms, 10.8MB)
# 테스트 6 〉	통과 (0.31ms, 10.9MB)
# 테스트 7 〉	통과 (0.27ms, 10.9MB)
# 테스트 8 〉	통과 (0.28ms, 10.9MB)
# 테스트 9 〉	통과 (0.30ms, 11MB)
# 테스트 10 〉	통과 (0.30ms, 10.9MB)
# 테스트 11 〉	통과 (0.28ms, 10.9MB)
# 테스트 12 〉	통과 (0.29ms, 11MB)
# 테스트 13 〉	통과 (0.36ms, 10.9MB)
# 테스트 14 〉	통과 (0.29ms, 10.9MB)
# 테스트 15 〉	통과 (0.33ms, 10.9MB)
# 테스트 16 〉	통과 (0.29ms, 10.9MB)
# 테스트 17 〉	통과 (0.29ms, 10.9MB)
# 테스트 18 〉	통과 (0.28ms, 11MB)
# 테스트 19 〉	통과 (0.30ms, 11MB)
# 테스트 20 〉	통과 (0.31ms, 11MB)
# 테스트 21 〉	통과 (0.28ms, 10.9MB)
# 테스트 22 〉	통과 (0.29ms, 10.9MB)
# 테스트 23 〉	통과 (0.30ms, 10.9MB)
# 테스트 24 〉	통과 (0.29ms, 10.9MB)
# 테스트 25 〉	통과 (0.28ms, 10.9MB)
# 테스트 26 〉	통과 (0.29ms, 10.9MB)
# 테스트 27 〉	통과 (0.29ms, 10.9MB)
# 테스트 28 〉	통과 (0.29ms, 10.9MB)
# 테스트 29 〉	통과 (0.42ms, 10.9MB)
# 테스트 30 〉	통과 (0.33ms, 10.9MB)
# 테스트 31 〉	통과 (0.29ms, 10.9MB)
# 테스트 32 〉	통과 (0.29ms, 10.9MB)
import re
def solution(dartResults):
    tokens = re.split(r'(\d+|[SDT]|[*#])', dartResults)
    number = re.compile(r'\d')
    score= re.compile('[SDT]')
    option = re.compile('[*#]')

    answer = []
    for token in tokens:
        if token == '':
            continue
        if number.match(token):
            answer.append(int(token))
        elif score.match(token):
            if token == "D":
                answer[-1] **= 2
            elif token == "T":
                answer[-1] **= 3
        if option.match(token):
            if token == "*":
                answer[-1] *= 2
                try: answer[-2] *= 2
                except: pass
            elif token == "#":
                answer[-1] *= -1 
    return sum(answer)