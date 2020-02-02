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

# from collections import Counter
# def solution(prices):
#     prices_counter = Counter(prices)
#     # sort twice?

#     answer = []
#     return answer
