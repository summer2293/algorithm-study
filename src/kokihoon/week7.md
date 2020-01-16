# week7

### 모의고사

```python
from itertools import cycle

def solution(answers):
    answer = []
    count = [0,0,0]
    player_1 = [1,2,3,4,5]
    player_2 = [2,1,2,3,2,4,2,5]
    player_3 = [3,3,1,1,2,2,4,4,5,5]

    for p1, p2, p3, answer in zip(cycle(player_1), cycle(player_2), cycle(player_3), answers) :
        if p1 == answer :
            count[0] += 1
        if p2 == answer :
            count[1] += 1
        if p3 == answer :
            count[2] += 1

    max_num = max(count)

    for i in range(len(count)) :
        if count[i] == max_num :
            answer.append(i+1)

    return answer
```

### 완주하지 못한 선수

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()

    for par, com in zip(participant, completion) :
        if par != com :
            return par

    return participant[-1]
```

### 자릿수 더하기

```python
def solution(n):
    answer = 0

    for i in str(n):
        answer = answer + int(i)

    return answer
```

### 예산

```python
def solution(d, budget):
    answer = 0
    sum = 0

    d.sort()

    for i in range(len(d)) :
        if sum + d[i] <= budget :
            answer += 1
            sum += d[i]

    return answer
```

### 실패율

```python
import operator

def solution(N, stages):
    length = len(stages)
    answer = []
    sum = 0
    stages.sort()
    j = 1
    k = 0

    while k < len(stages) :
        if stages[k] == j :
            sum +=1
            k += 1
        else :
            answer.append(sum/length)
            length -= sum
            sum = 0
            j += 1

    answer.append(sum/length)
    answer = answer[0:N]
    answer1 = []
    for idx, val in enumerate(answer):
        answer1.append((idx+1, val))

    answer2 = sorted(answer1, key=operator.itemgetter(1), reverse=True)
    answer3 = []
    for (i, d) in answer2 :
        answer3.append(i)

    return answer3

```

### 다트 게임

```python
import re

def solution(dartResult):

    answer = 0
    result = []

    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)

    for index, score in enumerate(scores):
        num = int(score[0])
        bouns = score[1]
        option = score[2]

        if bouns == 'S' :
            bouns = 1
        elif bouns == 'D' :
            bouns = 2
        elif bouns == 'T' :
            bouns = 3

        if option == '*' :
            if index == 0 :
                result.append(num**bouns*2)
            else :
                result[index-1] *= 2
                result.append(num**bouns*2)
        elif option == '#' :
            result.append(num**bouns*-1)
        else :
            result.append(num**bouns)
    answer = sum(result)

    return answer
```

## 개별문제

### 문자열압축

> 데이터 처리 전문가가 되고 싶은 어피치는 문자열을 압축하는 방법에 대해 공부를 하고 있습니다. 최근에 대량의 데이터 처리를 위한 간단한 비손실 압축 방법에 대해 공부를 하고 있는데, 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현하는 알고리즘을 공부하고 있습니다.

> 간단한 예로 aabbaccc의 경우 2a2ba3c(문자가 반복되지 않아 한번만 나타난 경우 1은 생략함)와 같이 표현할 수 있는데, 이러한 방식은 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다. 예를 들면, abcabcdede와 같은 문자열은 전혀 압축되지 않습니다. 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을 찾아보려고 합니다.

> 예를 들어, ababcdcdababcdcd의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면 2ab2cd2ab2cd로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 2ababcdcd로 표현할 수 있으며, 이때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.

> 다른 예로, abcabcdede와 같은 경우, 문자를 2개 단위로 잘라서 압축하면 abcabc2de가 되지만, 3개 단위로 자른다면 2abcdede가 되어 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

> 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

##### 제한 사항

- s의 길이는 1 이상 1,000 이하입니다.
- s는 알파벳 소문자로만 이루어져 있습니다.

##### 입출력 예

| s                        | result |
| ------------------------ | ------ |
| aabbaccc                 | 7      |
| ababcdcdababcdcd         | 9      |
| abcabcdede               | 8      |
| abcabcabcabcdededededede | 14     |
| xababcdcdababcdcd        | 17     |

##### 입출력 예 설명

입출력 예 #1

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #2

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #3

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #4

문자열을 2개 단위로 자르면 abcabcabcabc6de 가 됩니다.
문자열을 3개 단위로 자르면 4abcdededededede 가 됩니다.
문자열을 4개 단위로 자르면 abcabcabcabc3dede 가 됩니다.
문자열을 6개 단위로 자를 경우 2abcabc2dedede가 되며, 이때의 길이가 14로 가장 짧습니다.

입출력 예 #5

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.

#### 접근 방식

> 맨 처음부터 문자열을 쪼개서 접근하기 때문에 문자열을 다 검사할 필요가 없고 절반 정도로 끊어서 검사하면 된다. 처음에는 이생각을 못했었는데 풀이를 보고 이해하였다.
> 처음부터 for 문 돌다가 이전 값이랑 비교를 해서 같으면 이전 값이랑 더해주고 다르면 이전값이 저장이 되고 현재 값이 초기화 된다.

```python
def solution(s):

    if len(s)==1:
        return 1

    answer = len(s)

    half_len = int(len(s)/2)

    for i in range(1,half_len+1):
        start = i
        res = []
        pre_s = s[0:i]
        num = 1
        while True:
            now_s = s[start:start+i]
            if now_s == pre_s:
                num += 1
            else :
                res.append([num, pre_s])
                num = 1
                pre_s = now_s
            if start > len(s):
                break
            start += i

        half_len = 0

        for j in range(len(res)):
            if res[j][0] == 1:
                half_len += len(res[j][1])
            else :
                half_len += len(str(res[j][0]))
                half_len += len(res[j][1])

        answer = min(answer, half_len)
    return answer
```
