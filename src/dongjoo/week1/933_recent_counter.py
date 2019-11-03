# 1st attempt
from collections import deque

class RecentCounter:

    def __init__(self):
        self.que = deque()
        

    def ping(self, t: int) -> int:
        self.que.append(t)
        while (self.que)[0] < t - 3000:
            # print(self.que, "que", t-3000)
            self.que.popleft()
        return len(self.que)

# commands = ["ping","ping","ping","ping"]
# inputs = [[1],[100],[3001],[3002]]
# answer = RecentCounter()

# for i in range(len(commands)):
#     operation = "answer." + str(commands[i]) + "(" + str(inputs[i][0]) + ")"
#     # print(operation)
#     print(eval(operation))

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Result:
# Runtime: 324 ms, faster than 98.24 % of Python3 online submissions for Number of Recent Calls.
# Memory Usage: 18.5 MB, less than 20.00 % of Python3 online submissions for Number of Recent Calls.
