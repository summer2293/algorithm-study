#### Jandercase 만들기 https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    flag = True
    for char in s:
        if char == " ":
            answer += char.lower()
            flag = True
        else:
            if flag:
                flag = False
                answer += char.upper()
            else:
                answer += char.lower()
    return answer