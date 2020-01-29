# programmes lv2. 주식가격 
# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    prices = deque(prices)
    answer = []
    while(prices):
        count = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price <= next_price:
                count +=1
            else:
                count +=1
                break
        answer.append(count)
    return answer
