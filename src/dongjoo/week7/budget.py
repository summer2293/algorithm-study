# https://programmers.co.kr/learn/courses/30/lessons/12982  

import heapq


def solution(d, budget):
    heapq.heapify(d)
    answer = 0
    while budget > 0 and d and budget >= d[0]:
        budget -= heapq.heappop(d)
        answer += 1
    return answer

# time complexity linear for heapify + answer * log(length of d)
# space complexity: nothing other than just the linear input size

print(solution([2, 2, 3, 3], 10), "is the answer")
