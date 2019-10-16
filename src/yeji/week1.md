# 프로그래머스 프린터
```python
def solution(priorities.location):

    while len(priorities) != 0:

        if priorities[0] == max(priorities):

            answer += 1

            priorities.pop(0)

            if location == 0:

                return answer

            else:

                location -= 1

        else:

            priorities.append(priorities.pop(0))

            if location == 0:

                location = len(priorities) -1

            else:

                location -= 1

        return answer
```


# Leetcode- Number of Recent Calls
```python
class Solution:
	def isValid(self, s:str):
		self.characters = {'(':')','{':'}','[':']'}
		stack = []
		for i in s:
			if i in self.characters:
				stack.append(i)
			else:
				if not stack:
					return False
				else:
					if i == self.characters[stack[-1]]:
						stack.pop()
					else:
						return False
			if stack:
				return False
			else:
				return True
```
# Leetcode - MinStack

```python
class MinStack:

    def __init__(self):

        """

        initialize your data structure here.

        """

        self.data = []

    def push(self, x: int) :

        if not len(self.data):

            self.data.append((x,x))

        else:

            self.data.append((x,min(self.data[-1][1],x)))

    def pop(self) -> None:

        self.data.pop()

    def top(self) -> int:

       return self.data[-1][0]

    def getMin(self) -> int:

       return self.data[-1][1]
```


# LeetCode - Number of recent calls

```python

```

# LeetCode - Maximum SubArray
```python

```

# LeetCode - Climbing Stairs

```python

```