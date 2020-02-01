# https: // programmers.co.kr/learn/courses/30/lessons/60058
def flip(brackets):
    brackets = brackets.replace("(", "t")
    brackets =  brackets.replace(")", "(")
    brackets = brackets.replace("t", ")")
    return brackets

def correct(brackets):
    stack = 0
    for bracket in brackets:
        if bracket == "(":
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return stack == 0



def solution(brackets):
    if not brackets:
        return ''
    
    left_count = 0
    right_count = 0
    u_index = 0
    # find first u, v
    for i in range(len(brackets)):
        if brackets[i] == "(":
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            u_index = i
            break

    if correct(brackets[:u_index+1]):
        return brackets[:u_index+1] + solution(brackets[u_index+1:])
    return "(" + solution(brackets[u_index+1:]) + ")" + flip(brackets[:u_index+1][1:-1])


# time complexity: 안 좋을 듯, string에 대한 concatenation과 replace 작업 등, immutable 타입 관련 작업 많음. at least n **2
# space complexity: n
# maybe come up with proof of why this always resuls in correct format, should be easy
