# https://programmers.co.kr/learn/courses/30/lessons/17687

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
def convert_decimal(n, b):
    if b <= 10:
        if n < b:
            return str(n)
        return convert_decimal(n//b, b) + str(n % b)
    # bigger than 10
    if n < b:
        return lst[n]
    return convert_decimal(n//b, b) + lst[n%b]

def solution(n, t, m, p):
    order = 0 # whose turn is it
    num = 0 # current number in decimal
    num_converted = '0' # current number in base n, in string
    answer = []
    while len(answer) < t:
        print('outer while, num, num_converted', num, num_converted)
        print('converted', convert_decimal(num, n))
        # iterate until playser's turn
        while order + len(num_converted) < p:
            order += len(num_converted)
            num_converted = convert_decimal(num+1, n)
            num += 1
        # append what player has to say
        print('bewteen while =>', 'num_converted: ',num_converted, 'p: ', p, 'order:',  order)
        answer.append(num_converted[p-order-1])
        # iterate until cycle (of length m)is over, restart from order 0
        while order + len(num_converted) < m:
            order += len(num_converted)
            num_converted = convert_decimal(num+1, n)
            num += 1
        num_converted = num_converted[(order + len(num_converted) - m):]
        print('end', num_converted)
        order = 0
        print(num_converted, "num converted")
        print(num, "num")

    return ''.join(answer)


# print(solution(2,4,2,1))
# print(solution(16,16,2,2,))
print(solution(4,3,5,3))
