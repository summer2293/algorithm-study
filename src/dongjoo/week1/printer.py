# kinda difficult because have to keep count of what the 
# "maximum" priority is to decide whether to send to back or not
# can be done in a lot of ways but did it with a stack that's 
# basically a sorted priorities, popping the "max" if the element
# at the "head" of queue has "max priority"
# space complexity o(n) for stack
# ime complexity o(nlogn) for sort

# maybe explain that deque can't be mutated during iteration
# to fellow study members
from collections import deque
def solution(priorities, location):
    answer = 0
    # index variable to keep track of "location"
    idx = location
    queue = deque(priorities)
    stack = sorted(priorities)
    while queue:
        print("stack", stack)
        print("q", queue)
        print(answer, idx, "answer, idx")
        elem = queue.popleft()
        if elem != stack[-1]:
            queue.append(elem)
            # decrease index of important file
            idx -= 1
            if idx < 0:
                idx = len(queue) - 1
        else:
            stack.pop()
            idx -= 1
            answer += 1
            if idx < 0:
                return answer
    return answer


answer = solution([1, 1, 9, 1, 1, 1],0)
# answer = solution([2, 1, 3, 2],2)

print(answer)
