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