# [124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899)

```python

def solution(n):
    answer = ''

    num_dict = {1:"1",2:"2",0:"4"}
    mok = 1
    na = 1
    
    while mok != 0:
        mok = n //3
        na = n % 3
        
        if na == 0 :
            mok -= 1
            
        n = mok
            
        answer = num_dict[na] + answer
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.8MB)
# 테스트 7 〉	통과 (0.05ms, 10.6MB)
# 테스트 8 〉	통과 (0.04ms, 10.6MB)
# 테스트 9 〉	통과 (0.04ms, 10.6MB)
# 테스트 10 〉	통과 (0.04ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.6MB)
# 테스트 14 〉	통과 (0.04ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.10ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.7MB)
```