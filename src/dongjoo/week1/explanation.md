# dynamic programming/동적 프로그래밍

### 정의: dynamic programming usually refers to simplifying a decision by breaking it down into a sequence of decision steps over time.

### 특징: 1. optimal substructure 2. overlapping sub-problem
- optimal substructure: 문제의 최적해가 subproblem들의 최적해를 사용해서 얻어 지는 성질
- overlapping sub-problem: 동일한 subproblem들이 많이 발생할 때 -> combines solutions to sub-problems.

*(divide and conquer: subproblems 들이 overlapping 하지 않을 때)*

### 활용: Dijkstra's shortest path algorithm, Bellman Ford.... 코테...

### in short : 큰 문제에 닮음꼴의 작은 문제가 깃든다
* 관계중심으로 파악함으로써 문제를 간명하게 볼 수 있다
* but... 재귀적 해법을 사용하면 심한 중복 호출이 일어나는 경우가 있다

### 접근법:
1. memoization: Top Down, hashtable과 같은 자료구조를 사용해서 연산을 하기 전, 먼저 연산이 되었는지 확인, 연산이 되었다면 연산된 결과값 사용 O(1), 연산이 안되어 있다면 연산 진행
2. tabulation: 0번째 subproblem 부터 build-up을 시작, n번째 답 (array의 n-1 번째) 값 return

example (fibonacci):

``` python
# -------------------- tabular
def tabular(n):
    for i in range(n):
        f[i] = f[i-1] + f[i-2]
    return (f[n])
# -------------------- memo
def memo(n):
    if (lookup[n] == None)
        if (n <= 1)
            lookup[n] = n
        else
            lookup[n] = memo(n-1) + memo(n-2)
return lookup[n]
# -------------------- recursive
def recur(n):
    if (n <= 1)
        return n
    return recur(n-1) + recur(n-2)

```

 example:
 - leetcode 70번, climb staris 문제 https://www.youtube.com/watch?v=5o-kdjv7FD0&t=194s
 fun fact, can be solved without dp

- leetcode 53번: 
``` python
class Solution:
    def maxSubArray(self, nums):
        # use input to save space, for memoization
        maximum = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            maximum = max(nums[i], maximum)
        return maximum
```




# sources:
https://en.wikipedia.org/wiki/Dynamic_programming
https://www.youtube.com/watch?v=OQ5jsbhAv_M
https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/
