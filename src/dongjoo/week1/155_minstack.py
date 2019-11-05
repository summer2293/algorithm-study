# 1st attempt
# couldn't think of way to get min in constant time
# but utilized a minimum variable and the index that points to that
# in order to keep track of when the min gets popped and recalculate
# minimum if minimum gets popped
# this will yield n squared time when the input is given in 
# decreasing order and pop and getMin are alternately called
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None
        self.minindex = None
    def push(self, x: int) -> None:
        # print("push, stack", self.stack)
        self.stack.append(x)
        if len(self.stack) == 1:
            self.minindex = 0
            self.minimum = x
        else:
            if x < self.minimum:
                self.minimum = x
                self.index = len(self.stack)-1
    def pop(self) -> None:
        # print("pop, stack", self.stack)
        self.stack.pop()
        # recalculate min when minimum gets popped and stack isn't empty
        if len(self.stack) >= self.minindex and self.stack:
            # start again from 0 to find min
            self.minimum = self.stack[0]
            self.minindex = 0
            for idx in range(len(self.stack)):
                if self.stack[idx] < self.minimum:
                    self.minimum = self.stack[idx]
                    self.minindex = idx
        elif not self.stack:
            self.minimum = None
            self.minindex = None
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minimum

        
answer = MinStack()
answer.push(-2)
answer.push(0)
answer.push(-3)
print(answer.getMin())
answer.pop()
print(answer.top())
print(answer.getMin())

["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
[[], [-2], [0], [-3], [], [], [], []]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# some other guy's answer, really smart


# class MinStack:


# def __init__(self):
#     self.q = []

# # @param x, an integer
# # @return an integer


# def push(self, x):
#     curMin = self.getMin()
#     if curMin == None or x < curMin:
#         curMin = x
#     self.q.append((x, curMin))

# # @return nothing


# def pop(self):
#     self.q.pop()


# # @return an integer
# def top(self):
#     if len(self.q) == 0:
#         return None
#     else:
#         return self.q[len(self.q) - 1][0]


# # @return an integer
# def getMin(self):
#     if len(self.q) == 0:
#         return None
#     else:
#         return self.q[len(self.q) - 1][1]
