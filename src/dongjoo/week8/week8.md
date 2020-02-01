```python

# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        days = 0
        # print(prices[i], "cocmpared with, outer loop")
        for price in prices[i+1:]:
            days += 1
            if price < prices[i]:
                break
        answer.append(days)
    return answer

# time complexity: n squared
# space complexity: linear to produce answer, maybe overwrite input to make space constant? 

print(solution([1, 2, 3, 2, 3]))


# https://programmers.co.kr/learn/courses/30/lessons/62048
from fractions import Fraction
def solution(w, h):
    if w == h:
        return w ** 2 - w

    frac = Fraction(w,h)
    new_w = frac.numerator
    new_h = frac.denominator
    num_split =  new_w + new_h - 1
    # print(num_split, "num split")
    num_rectangles = w // new_w
    # print(num_rectangles, "num recta")
    return w * h - num_rectangles * num_split 


print(solution(8,12))


# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    # arr to keep track of entering/exit order and ID
    # 1st element: 1 for enter 0 for exit, 2nd element: uid
    enter_exit_id = []
    entered_message = "님이 들어왔습니다."
    exit_message = "님이 나갔습니다."
    # dictionary to keep track of  key: user id, value: most recent nickname
    user_dict = dict()
    answer = []

    # change_count = 0

    for message in record:
        # print(enter_exit_id, i, "enter exit, id")
        action = message.split(' ')
        if action[0] == 'Enter':
            enter_exit_id.append([1, action[1]])
            user_dict[action[1]] = action[2]
        elif action[0] == 'Leave':
            enter_exit_id.append([0, action[1]])
        else:
            user_dict[action[1]] = action[2]
            # change_count += 1

    for log in enter_exit_id:
        message = ""
        if log[0]:
            message = user_dict[log[1]] + entered_message
        else:
            message = user_dict[log[1]] + exit_message
        answer.append(message)

    return answer



# https://programmers.co.kr/learn/courses/30/lessons/60058
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



# https: // programmers.co.kr/learn/courses/30/lessons/12899
remainder_dict = {0:'4', 1:'1', 2:'2'}

def solution(n):
    # print(n, end=' ')
    if not n:
        return '0'
    if n == 3:
        return '4'
    return recursive_ternary(n)

def recursive_ternary(n):
    # print("input is ", n)
    # base case
    if n == 0:
        return ''
    if n < 3:
        return remainder_dict[n]
    # recursive case:
    remainder = remainder_dict[n % 3]
    if n / 3 > 4:
        if (n%3==0):
            return recursive_ternary(n//3 -1) + remainder
        return recursive_ternary(n//3) + remainder
    else:
        if n /3 <= 2:
            return '1' + remainder
        elif n/3 <= 3:
            return '2' + remainder
        elif n / 3 <= 4:
            return '4' + remainder



```