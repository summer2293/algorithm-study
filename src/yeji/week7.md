# [Programmers - 자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931)

```python

def solution(n):
    answer = 0
    
    lst = [int(i) for i in str(n)]
    
    for i in range(len(lst)):
        
        answer += lst[i]
    
    return answer

```