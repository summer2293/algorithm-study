# programmers lv1 문자열 압축 
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    if len(s) == 1: 
        return 1
        
    answer = len(s)
    for token in range(1,len(s)):
        result = len(s)
        if len(s)//token <= 1: break
        count, flag = 0, ''
        for idx in range(len(s)//token):
            tmp = idx * token   
            if idx == 0: 
                flag = s[tmp:token+tmp]
                count += 1
                continue
            if flag == s[tmp:token+tmp]: 
                count += 1
            else:
                if count > 1:
                    result -= count_check(token, count)
                flag = s[tmp:token+tmp]
                count = 1 
                continue
            if idx == (len(s)//token)-1 and count > 1:
                result -= count_check(token, count)
        answer = min(result, answer)
    return answer


def count_check(token, count):
    before = count*token
    after = len(str(count))+token
    if before > after:
        return (before - after)      
    return 0