# [프로그래머스-모의고사](https://programmers.co.kr/learn/courses/30/lessons/42840)

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
                
    maxV = max(count1, count2)
    maxV = max(maxV, count3)
    
    answer = []

    if maxV == count1:
        answer.append(1)
    if maxV == count2:
        answer.append(2)
    if maxV == count3:
        answer.append(3)       
    return answer
```

# [프로그래머스-소수찾기](https://programmers.co.kr/learn/courses/30/lessons/42839)

```python


```

# [프로그래머스-숫자야구](https://programmers.co.kr/learn/courses/30/lessons/42841)

```python

```

# [프로그래머스-카펫](https://programmers.co.kr/learn/courses/30/lessons/42842)

```python
# 빨간색과 갈색의 색칠된 격자의 수만 기억함,
# (빨간 격자 세로 길이 *2)+ (빨간 격자 가로 길이*2) + 4(모서리)
# 빨간 격자 세로길이 
# 빨간색 가로 - a 세로 - b red = a*b brown = 2(A+B)+4
def solution(brown, red):
    for a in range(1,int(red**0.5)+1):
        if not red % 2 or red % 2 != 0:
            b = red
            if 2*a + 2*b + 4 == brown:
                return [b+2,a+2]

# 테스트케이스 두개성공...

```

# [leetcode-find_the_town_judge](https://leetcode.com/problems/find-the-town-judge/)

```python
# 마을엔 1부터  N으로 표기되는 N명의 사람들이 있다. 이들 중 한사람이 비밀스러운 마을 판사라는 소문이 있다.
# 만약, 마을판사가 존재한다면
# 1. 마을판사는 아무도 신뢰하지 않는다.
# 2. 모든사람들(마을판사를 제외한)은 마을판사를 신뢰한다.
# 3. 위의 1,2 조건을 만족하는 사람은 딱 한명 뿐이다.
# trust[i] = trust[a,b] a가 b를 신뢰한다는 의미이다.
```

# [leetcode-regions-cut-by-slashes](https://leetcode.com/problems/regions-cut-by-slashes/)

```python
```