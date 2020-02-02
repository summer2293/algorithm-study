# 개선해본 코드
def solution(p):
    if correct(p) is True: return p 
    
    idx = balance(p) + 1
    u, v = p[:idx],  p[idx:]
    if correct(u): return u + solution(v)
    else: return "(" + solution(v) + ")" + swap(list(u)[1:-1]) 

# left, right 변수 1개로 변경 
def correct(p):
    count = 0 
    for char in p:
        if char == "(": count += 1
        else: count -= 1
        if count < 0: return False
    return True


def balance(p):
    count = 0
    for idx, char in enumerate(p):
        count = count-1 if char == "(" else count+ 1
        if count == 0: return idx

def swap(u):
    answer = ''
    for char in u:
        if char == "(": answer += ")"
        else: answer += "("
    return answer

# 내 코드 
def solution(p):
    answer = ''
    
    # 1. 빈문자 or 올바른 문자 check()
    if correct(p) is True: return p
    
    # 2. 올바른 u
    u, v = p[:balance(p)],  p[balance(p):]
    if correct(u): 
        return u + solution(v)
    
    # 올바르지 않은 u
    answer = "(" + solution(v) + ")"
    for char in list(u)[1:-1]:
        if char == "(":
            answer += ")"
        else: 
            answer += "("
    return answer


def correct(p):
    left, right = 0, 0
    for char in p:
        if char == "(": 
            left += 1
        else: 
            if left != 0: left -= 1
            else: right += 1
    if left == right == 0: return True

def balance(p):
    count = 0
    for idx, char in enumerate(p):
        count = count-1 if char == "(" else count+ 1
        if count == 0: return idx + 1