# [Programmers - 자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)

```python

def solution(n):
    answer = 0
    
    lst = [int(i) for i in str(n)]
    
    for i in range(len(lst)):
        
        answer += lst[i]
    
    return answer

```

# [Programmers - 모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)

```python

def solution(answers):
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    
    count1=0
    count2 = 0
    count3 = 0
    
    for i in range(len(answers)):
        if answers[i] == stu1[i%5]:
            count1 += 1
        
        if answers[i] == stu2[i%8]:
            count2 += 1
        
        if answers[i] == stu3[i%10]:
            count3 += 1
                
    maxV = max(count1, count2, count3)
    
    answer = []

    if maxV == count1:
       print(answer.append(1))
    if maxV == count2:
        print(answer.append(2))
    if maxV == count3:  
        print(answer.append(3))
    return answer


```

# [programmers - 콜라츠 추측] (https://programmers.co.kr/learn/courses/30/lessons/12943)

```python
def solution(n):
    answer = 0

    for answer in range(500):
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 +1
        if n == 1:
            return answer + 1
    return -1

# testcase 13 실패

def solution(n):
    answer = 0
    for answer in range(500):
        n = n / 2 if n % 2 == 0 else n * 3 + 1
        if n == 1:
            return answer + 1
    return -1
    
# testcase 13 실패

```

```pyhton

삼항 연산자 (Tenary operators)

참인 경우 값 if 조건 else 거짓인 경우 값


```

# [Programmers - 완주하지 못한 선수] (https://programmers.co.kr/learn/courses/30/lessons/42576)

```python



```

# [Programmers - 예산] (https://programmers.co.kr/learn/courses/30/lessons/12982)

```python

```

# [Programmers - [1차]다트 게임](https://programmers.co.kr/learn/courses/30/lessons/17682)

```python

```

# [Programmers - 실패율] (https://programmers.co.kr/learn/courses/30/lessons/42889)

```python

```