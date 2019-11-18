## 모의고사 (수포자)

```python
def solution(answers):    
    st1 = [1, 2, 3, 4, 5]
    st2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    st_box = [0] * 3
    result = []
    for i,v in enumerate(answers):
        if (st1[i % len(st1)] == v):
            st_box[0] += 1
        if (st2[i % len(st2)] == v):
            st_box[1] += 1
        if (st3[i % len(st3)] == v):
            st_box[2] += 1         
    
    return [i + 1 for i, v in enumerate(st_box) if v == max(st_box)]
# 테스트 1 〉	통과 (0.07ms, 10.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.05ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.8MB)
# 테스트 5 〉	통과 (0.06ms, 10.8MB)
# 테스트 6 〉	통과 (0.07ms, 10.7MB)
# 테스트 7 〉	통과 (1.73ms, 11MB)
# 테스트 8 〉	통과 (0.59ms, 10.9MB)
# 테스트 9 〉	통과 (3.12ms, 13.7MB)
# 테스트 10 〉	통과 (1.43ms, 11.1MB)
# 테스트 11 〉	통과 (3.20ms, 14MB)
# 테스트 12 〉	통과 (2.88ms, 13.2MB)
# 테스트 13 〉	통과 (0.21ms, 10.8MB)
# 테스트 14 〉	통과 (3.26ms, 14.4MB)
```

## 카펫
```python
def solution(brown, red):
    square = brown + red
    for i in range(3,square+1):
        if square % i == 0:
            width = max(i, square//i)
            height = min(i, square//i)
            if (width - 2) * (height - 2) == red:
                return[width, height]
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.10ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.07ms, 10.6MB)
# 테스트 7 〉	통과 (0.09ms, 10.7MB)
# 테스트 8 〉	통과 (0.10ms, 10.7MB)
# 테스트 9 〉	통과 (0.10ms, 10.7MB)
# 테스트 10 〉	통과 (0.10ms, 10.7MB)
```

## 소수찾기

```python
# 소수찾기  - 미구현 안돌아감 ㅠㅠ 
import itertools
def solution(numbers):
    for i in range(2,len(numbers)+1):
        a = list(map(''.join, itertools.permutations(numbers,i)))
        a = list(map(lambda x: int(x), a))
        a = list(set(a))
        print(a)
        
        for i in a:
            is_prime(i)
            # print(is_prime(int(i)))
              
def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
            else:
                return True
    else:
        return False
```

## 야구

```python
# 미구현 ㅠㅠ 아예 못품 
def solution(baseball):
    numbers = [] * 865
    for i in range(123,987+1):
        numbers.append(i)
    print(len(numbers))

    for i in numbers:
        h = i//100
        m = (i//10) % 10
        f = i % 10 
        if (h * m * f == 0):
            numbers.remove(i)
        elif ((h==m) or(m==f) or (h==f)):
            numbers.remove(i)
    
    print(len(numbers))
```





## 959.Regions Cut By Slashes.py

```python
# 안돌아감. 문제 잘못 접근 ㅠㅠ 두시간 잡고있었는데 다흑 
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        len2 = len(grid) * 2
        list = [[0 for i in range(len2) ] for j in  range(len2)]
        line = 0
        x = 0
        for r,v in enumerate(grid):
            for c, m in enumerate(v):
                if (m == "/"):
                    list[r*2][c*2+1] += 1
                    list[r*2+1][c*2] += 1
                elif (m == "\\"):
                    list[r*2][c*2] = 1
                    list[r*2+1][c*2+1] = 1
        
        

        for i in range(0,len2,2):
            for j in range(len2):
                r = i
                c = j
                count = 0
                flag = 0
                if (i == j and i != 0):
                    continue
                elif j % 2 == 0:               
                    while(c < len2 and r < len2):
                        flag += 1
                        if list[r][c] == 1:
                            count += 1
                        r +=1
                        c += 1
                else:
                    while(c >= 0 and r < len2):
                        flag += 1
                        if list[r][c] == 1:
                            count += 1
                        r += 1
                        c -= 1

                # print(flag, count, i, j)
                if (flag == count):
                    if(i+j+1 != len2):
                        line += 1
                    if (count == len2):
                        x += 1
        # print(line, x)
        
        for i in list:
            print(i)
        if x == 2:
            return 4
        else:
            return line + x + 1
```

## 997. Find the Town Judge


```python
## trash code 
## 오ㅜ분남아떠 ㅠㅠㅠㅠㅠㅠ다시고칠것
#Runtime: 1180 ms, faster than 5.01% of Python3 online submissions for Find the #Town Judge.
#Memory Usage: 23.9 MB, less than 10.00% of Python3 online submissions for Find #the Town Judge.
import operator
from collections import Counter
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        list = [[0 for i in range(N+1) ] for j in  range(N+1)]
        people = []
        counter = {}
        for i in trust:
            list[i[0]][i[1]] = i[1]
            try:     
                counter[i[1]] += 1
            except:
                counter[i[1]] = 1
        
        p = max(counter, key=lambda key: counter[key])
        
        sum = 0 
        for i in list[p]:
            sum+=i
            if sum >= 1:
                return -1
        
        value = sorted(counter.values())
        
        if(len(value) > 1 and value[-1] == value[-2]):
            return -1

        return p
```