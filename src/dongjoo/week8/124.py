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


for i in range(1,30):
    print(solution(i))

# look into divmod

# test ternary correctness
# print(recursive_ternary(102), 102)
# print(int('1212', 4))
# print(solution(6))
# print(recursive_ternary(6))
