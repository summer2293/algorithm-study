## 알고리즘과제
### 프로그래머스 프린터
<pre>
<code>
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
</code>
</pre>


<hr/>
### Leetcode- Number of Recent Calls
<pre>
<code>
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
</code>
</pre>
<hr/>

### Leetcode - MinStack

<pre>
<code>
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
</code>
</pre>

<hr/>


### LeetCode - Number of recent calls
<pre>
<code>

</code>
</pre>

### LeetCode - Maximum SubArray
<pre>
<code>
</code>
</pre>

### LeetCode - Climbing Stairs
<pre>
<code>
</code>
</pre>

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk0NjkxOTM1Nyw2NDk2MjQ3ODcsLTEyMT
g4NzEyMjZdfQ==
-->