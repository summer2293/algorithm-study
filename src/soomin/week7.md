## week7

#### 모의고사

```python
def solution(answers):
    # 이전 코드는 변수로, 지금은 arr 로 변경(확장성 위해 더 좋을거라 생각)
    students = [[1, 2, 3, 4, 5], 
                [2, 1, 2, 3, 2, 4, 2, 5], 
                [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i, student in enumerate(students):
        count = 0 
        for n, answer in enumerate(answers):
            order = n % len(student)
            if student[order] == answer:
                count += 1
        students[i] = count
    return [i + 1 for i, v in enumerate(students) if v == max(students)]
```

```python
# 테스트 1 〉	통과 (0.04ms, 10.8MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.07ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.06ms, 10.8MB)
# 테스트 6 〉	통과 (0.06ms, 10.8MB)
# 테스트 7 〉	통과 (1.88ms, 11.1MB)
# 테스트 8 〉	통과 (0.60ms, 10.9MB)
# 테스트 9 〉	통과 (3.43ms, 13.7MB)
# 테스트 10 〉	통과 (1.52ms, 11.1MB)
# 테스트 11 〉	통과 (3.88ms, 14MB)
# 테스트 12 〉	통과 (3.01ms, 13.3MB)
# 테스트 13 〉	통과 (0.22ms, 10.8MB)
# 테스트 14 〉	통과 (3.73ms, 14.5MB)
```

이전코드

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
```


#### 완주하지 못한 선수

```python
def solution(participant, completion):
    # counter 객체는 - + & | 연산이 가능하다함! 짱신기 
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```

```python
# 테스트 1 〉	통과 (0.20ms, 10.7MB)
# 테스트 2 〉	통과 (0.08ms, 10.7MB)
# 테스트 3 〉	통과 (0.23ms, 10.9MB)
# 테스트 4 〉	통과 (0.40ms, 11.1MB)
# 테스트 5 〉	통과 (0.43ms, 11.1MB)
# 효율성  테스트
# 테스트 1 〉	통과 (26.02ms, 87.3MB)
# 테스트 2 〉	통과 (42.64ms, 127MB)
# 테스트 3 〉	통과 (44.80ms, 154MB)
# 테스트 4 〉	통과 (64.97ms, 169MB)
# 테스트 5 〉	통과 (66.30ms, 167MB)
```

##### 이전코드 

```python
# def solution(participant, completion):
#     challenger = {}
    
#     for man in participant:
#         try: challenger[man] += 1
#         except: challenger[man] = 1
    
#     for man in completion:
#         challenger[man] -= 1
#         if challenger[man] == 0:
#             del challenger[man]
    
#     for i in challenger:
#         return i 
```


#### 자릿 수 더하기

```python
def solution(n):
    answer = 0
    while (n > 0):
        answer += n % 10
        n //= 10
    return answer
```

```python
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.03ms, 10.7MB)
# 테스트 7 〉	통과 (0.05ms, 10.8MB)
# 테스트 8 〉	통과 (0.04ms, 10.7MB)
# 테스트 9 〉	통과 (0.04ms, 10.7MB)
# 테스트 10 〉	통과 (0.04ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.6MB)
# 테스트 12 〉	통과 (0.05ms, 10.8MB)
# 테스트 13 〉	통과 (0.04ms, 10.7MB)
# 테스트 14 〉	통과 (0.04ms, 10.7MB)
# 테스트 15 〉	통과 (0.04ms, 10.7MB)
# 테스트 16 〉	통과 (0.04ms, 10.6MB)
# 테스트 17 〉	통과 (0.05ms, 10.7MB)
# 테스트 18 〉	통과 (0.04ms, 10.7MB)
# 테스트 19 〉	통과 (0.05ms, 10.7MB)
# 테스트 20 〉	통과 (0.04ms, 10.7MB)
# 테스트 21 〉	통과 (0.04ms, 10.7MB)
```

#### 실패율
```python
def solution(N, stages):
    failure = [0] * (N)
    user = len(stages)
    answer = dict()
    for i in stages:
        try: failure[i-1] += 1
        except: pass
    for i,value in enumerate(failure):
        try: answer[i+1] = value/user
        except: answer[i+1] = 0
        user -= value
    return [k for k, v in sorted(answer.items(), key=lambda item: item[1], reverse=True)]
```
```
# 테스트 1 〉	통과 (0.04ms, 10.8MB)
# 테스트 2 〉	통과 (0.13ms, 10.8MB)
# 테스트 3 〉	통과 (1.15ms, 15MB)
# 테스트 4 〉	통과 (7.75ms, 81.2MB)
# 테스트 5 〉	통과 (18.23ms, 157MB)
# 테스트 6 〉	통과 (0.16ms, 10.8MB)
# 테스트 7 〉	통과 (0.84ms, 14.5MB)
# 테스트 8 〉	통과 (7.60ms, 81.7MB)
# 테스트 9 〉	통과 (18.19ms, 158MB)
# 테스트 10 〉	통과 (7.52ms, 81.1MB)
# 테스트 11 〉	통과 (7.59ms, 80.5MB)
# 테스트 12 〉	통과 (11.76ms, 118MB)
# 테스트 13 〉	통과 (12.55ms, 125MB)
# 테스트 14 〉	통과 (0.06ms, 10.7MB)
# 테스트 15 〉	통과 (8.74ms, 54.9MB)
# 테스트 16 〉	통과 (2.70ms, 31.1MB)
# 테스트 17 〉	통과 (5.25ms, 54.9MB)
# 테스트 18 〉	통과 (2.64ms, 31.2MB)
# 테스트 19 〉	통과 (0.64ms, 12.2MB)
# 테스트 20 〉	통과 (3.83ms, 42.5MB)
# 테스트 21 〉	통과 (7.64ms, 75.8MB)
# 테스트 22 〉	통과 (18.40ms, 160MB)
# 테스트 23 〉	통과 (16.23ms, 153MB)
# 테스트 24 〉	통과 (15.00ms, 154MB)
# 테스트 25 〉	통과 (0.05ms, 10.6MB)
# 테스트 26 〉	통과 (0.04ms, 10.7MB)
# 테스트 27 〉	통과 (0.04ms, 10.7MB) 
```

#### 예산

```python
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break;
        answer += 1
    return answer
# 테스트 1 〉	통과 (0.03ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.7MB)
# 테스트 3 〉	통과 (0.04ms, 10.7MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.04ms, 10.7MB)
# 테스트 7 〉	통과 (0.04ms, 10.7MB)
# 테스트 8 〉	통과 (0.05ms, 10.7MB)
# 테스트 9 〉	통과 (0.05ms, 10.9MB)
# 테스트 10 〉	통과 (0.04ms, 10.8MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.07ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.8MB)
# 테스트 14 〉	통과 (0.05ms, 10.6MB)
# 테스트 15 〉	통과 (0.05ms, 10.7MB)
# 테스트 16 〉	통과 (0.05ms, 10.8MB)
# 테스트 17 〉	통과 (0.06ms, 10.8MB)
# 테스트 18 〉	통과 (0.05ms, 10.8MB)
# 테스트 19 〉	통과 (0.05ms, 10.8MB)
# 테스트 20 〉	통과 (0.04ms, 10.8MB)
# 테스트 21 〉	통과 (0.04ms, 10.7MB)
# 테스트 22 〉	통과 (0.04ms, 10.8MB)
# 테스트 23 〉	통과 (0.04ms, 10.8MB)
```

#### 다트게임

```python
# 다트게임 
import re
def solution(dartResults):
    # 숫자 / 문자 / 옵션을 다 분리해줌 
    tokens = re.split(r'(\d+|[SDT]|[*#])', dartResults)
    
    number = re.compile(r'\d')
    score= re.compile('[SDT]')
    option = re.compile('[*#]')

    answer = []
    for token in tokens:
        if token == '': # split 하면 '' 같은 문자열이 생기는데 잡지 못했음 
            continue
        if number.match(token):
            answer.append(int(token))
        elif score.match(token):
            if token == "D":
                answer[-1] **= 2
            elif token == "T":
                answer[-1] **= 3
        if option.match(token):
            if token == "*":
                answer[-1] *= 2
                try: answer[-2] *= 2
                except: pass
            elif token == "#":
                answer[-1] *= -1 
    return sum(answer)
```

```
# 다트게임 
# 테스트 1 〉	통과 (0.29ms, 10.8MB)
# 테스트 2 〉	통과 (0.29ms, 11MB)
# 테스트 3 〉	통과 (0.27ms, 10.9MB)
# 테스트 4 〉	통과 (0.32ms, 11MB)
# 테스트 5 〉	통과 (0.29ms, 10.8MB)
# 테스트 6 〉	통과 (0.31ms, 10.9MB)
# 테스트 7 〉	통과 (0.27ms, 10.9MB)
# 테스트 8 〉	통과 (0.28ms, 10.9MB)
# 테스트 9 〉	통과 (0.30ms, 11MB)
# 테스트 10 〉	통과 (0.30ms, 10.9MB)
# 테스트 11 〉	통과 (0.28ms, 10.9MB)
# 테스트 12 〉	통과 (0.29ms, 11MB)
# 테스트 13 〉	통과 (0.36ms, 10.9MB)
# 테스트 14 〉	통과 (0.29ms, 10.9MB)
# 테스트 15 〉	통과 (0.33ms, 10.9MB)
# 테스트 16 〉	통과 (0.29ms, 10.9MB)
# 테스트 17 〉	통과 (0.29ms, 10.9MB)
# 테스트 18 〉	통과 (0.28ms, 11MB)
# 테스트 19 〉	통과 (0.30ms, 11MB)
# 테스트 20 〉	통과 (0.31ms, 11MB)
# 테스트 21 〉	통과 (0.28ms, 10.9MB)
# 테스트 22 〉	통과 (0.29ms, 10.9MB)
# 테스트 23 〉	통과 (0.30ms, 10.9MB)
# 테스트 24 〉	통과 (0.29ms, 10.9MB)
# 테스트 25 〉	통과 (0.28ms, 10.9MB)
# 테스트 26 〉	통과 (0.29ms, 10.9MB)
# 테스트 27 〉	통과 (0.29ms, 10.9MB)
# 테스트 28 〉	통과 (0.29ms, 10.9MB)
# 테스트 29 〉	통과 (0.42ms, 10.9MB)
# 테스트 30 〉	통과 (0.33ms, 10.9MB)
# 테스트 31 〉	통과 (0.29ms, 10.9MB)
# 테스트 32 〉	통과 (0.29ms, 10.9MB)
```

## 개별문제

### 이상한 문자 만들기

> 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

##### 제한 사항

- 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
- 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

##### 입출력 예

| s               | return          |
| --------------- | --------------- |
| try hello world | TrY HeLlO WoRlD |

##### 입출력 예 설명

try hello world는 세 단어 try, hello, world로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 TrY, HeLlO, WoRlD입니다. 따라서 TrY HeLlO WoRlD 를 리턴합니다.



#### 접근 방식

> 처음에 생각한 접근법: 
>
> `s.split(' ')` 단어 분리 후 짝 홀수 구분하여 값 넣어주었다. 하지만 __공백이 여러개 들어 갈 수 있다는__ 생각을 못함 

```python
# 실패코드 
def solution(s):
    answer = ''
    tokens = s.split(" ")
    for token in tokens:
        for i,v in enumerate(token):
            if i % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
        answer += ' '
    return answer.strip()
```
##### 통과코드 

```python
def solution(s):
    answer = ''
    index = 0
    for v in s:
        if v == ' ':
            index = 0
            answer += v
        else:
            if index % 2 == 0:
                answer += v.upper()
            else:
                answer += v.lower()
            index += 1
    return answer
```

##### string concat

concat 문자열 += 해서 하는개 새 문자열을 반환하기 때문에 메모리 효율이 안좋다함. list.append() 이후 .join을 통해 문자열로 반환하는게 훨씬 메모리 사용에 좋다고한다.

보면 좋은 자료

<https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt>

```python
def solution(s):
    answer = []
    i = 0
    for token in s:
        if token == ' ':
            i = 0
            answer += token
        else:
            if i % 2 == 0:
                answer.append(token.upper())
            else:
                answer.append(token.lower())
            i += 1
    return "".join(answer)
```

