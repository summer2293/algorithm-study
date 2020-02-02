## happy new year - 설날 보너스 문제 모음

#### 1 . Jandercase 만들기 

##### 문제 내용 

JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다. 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

###### 제한 조건

- s는 길이 1 이상인 문자열입니다.
- s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
- 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )

###### 입출력 예

s						return
3people unFollowed me	3people Unfollowed Me
for the last week			For The Last Week

#### 내가 푼 코드
flag 를 써서 첫번째 값인지 check 했다. " " 를 만나거나 하면 새로운 문장의 시작이 되서 flag 를 true 상태로 만들어줌
```python
def solution(s):
    answer = ''
    flag = True
    for char in s:
        if char == " ":
            answer += char.lower()
            flag = True
        else:
            if flag:
                flag = False
                answer += char.upper()
            else:
                answer += char.lower()
    return answer
```

#### 코드 풀이 리뷰 

일단 알게된점

__title()__ 메서드

문자열의  시작하는 값의 문자를 capitalize 해줌. 공백도 그대로 

```python
>>> s = "hello    world"
>>> s.title()
'Hello    World'
```

그래서 예전에는 이 문제가 한줄로

```python
return s.lower().title()
```

로 가능했지만, 

```python
>>> s = "GIQGEK SAKDGDASKGLAKSDG  1abSDGANGNASGDKNL"
>>> s.lower().title()
'Giqgek Sakdgdaskglaksdg  1Absdgangnasgdknl'
```

##### 숫자가 앞에 나올경우 그 다음 값을 소문자로 만들어주기 때문에 이게 되지않는다고 한다. 

그래서 _이상한 문자 만들기_ 에서 했던 것 처럼 split 을 하지않고, flag 로  `" "` 를 만나면 그냥 answer += 를 해주는 식으로 진행하였다.

#### 다른사람의 쩌는 코드

```python
return ' '.join([word.capitalize() for word in s.split(" ")])
```

이게 되는 이유가 .split(" ") 를 할때 그 만큼 공백의 값을 만들어준다

```python
['GIQGEK', 'SAKDGDASKGLAKSDG', '', '1abSDGANGNASGD', '', '', '', '', '', '', '', '', 'KNL']
```

각각의 값을 capitalize 해준 후 join 으로 붙힌 코드가 인상적이었다.

이상한 문자 만들기는 각각의 값을 쪼개 처리를 해야 되었는데, 토큰을 쪼개 파이썬 내장 함수를 사용하는 간단한 것은 이렇게 풀 수 있구나! 생각함 그 전에 풀어봤던 문제가 머리에 남아있어 더 좋은 코드를 생각하지 못한게 조금 아쉽다. 





## 2. 조이스틱

조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.

ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

##### 제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.
입출력 예
name	return
JEROEN	56
JAN	23

#### 내가 푼 코드 

엄청 어려웠음...진심 하루종일 이거풀었음 ㅠㅡㅠ 몽총몽총 

```python

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def solution(name):
    answer =  0
	
    # 1. A 기준 자리 별 알파벳 움직여야할 숫자 횟수 계산! b > 1 c > 2 >
    count = change_cursor_count(name)

    # 2. 첫번째 위치 값 넣기 
    index = 0
    answer += count[index]
    count[index] = 0

    # 3. 다음에 움직일 값 찾기. 값을 돌면서 0으로 바꿔주고, sum 이 0 이되면 다 변경 한 것. 종료 
    while(sum(count) != 0):
        data  = find_next_index(index, count)
        index = data["index"]
        if index is not None: 
            answer += count[index] + data["move"]
            count[index] = 0
    
    return answer

def change_cursor_count(name):
    alphabet =[]
    for char in name:
        idx = ALPHABET.index(char)
        alphabet.append(min(idx, len(ALPHABET) - idx))
    return alphabet

def find_next_index(idx, count):
    for num in range(len(count)):
        ascending, descending  = (num+idx)%len(count), (len(count)-num+idx) % len(count) # 1, 2, 3, 4 and 10, 9, 8, 7
        if count[ascending] != 0: return {"index":ascending, "move":num}
        if count[descending] != 0: return {"index":descending, "move":num}
```


### 코드 풀이 리뷰

다른 사람 풀이를 보거나, 구글에 검색해도 명확하게 눈에 들어오는 코드가 없어서, __가독성 있는 코드를 짜려고 고려했음!__ 

이 알고리즘은 "그리디"로 현재 상황에서 어떤 선택을 하고, 그 상황에서 최적의 선택을 구해야 하는건데, 처음에 이걸 캐치 못하고 막무가내로 룰루랄라 풀다가 삽질함. 다음에는 어떻게 접근할 것인지 더 생각해보고 풀어야지..

##### 막힌 것

1. 다음 값을 asending 해주는 것만 생각하다가 엄청 삽질
2. 순차적으로 가는게 아니라, index 를 왔다갔다 거리는건데 for 문으로 시도해서 삽질 ++
3. 삽질이 더해가서 당떨어져서 이상한거 오타내고 삽질 +++ (밥먹으니 금방 해결 싱기!)



그래서 왼쪽, 오른쪽 비교해서 

```python
def solution(name):
    ... 
        next_value  = left_index(idx, count)
        check_value = right_index(idx, count)
        if (next_value[1] > check_value[1]):
            next_value = check_value
        idx = next_value[0]
	...
    return answer

def left_index(idx, count):
    for num in range(len(count)):
        if count[(num+idx)%len(count)] != 0:
            return [(num+idx)%len(count), num] # idx, move

def right_index(idx, count):
    for num in range(len(count), 0, -1):
        if count[(num+idx)%len(count)] != 0:
            return [(num+idx)%len(count), len(count)-num] # idx, move
```

이렇게 짰으나 너무 코드가 구려서 곰곰히 생각해본 결과, `(num+idx)%len(count), (len(count)-num+idx) % len(count)` 이렇게 해서 하나의 for 문을 써서 둘다 해결 해버림! 밥먹으니 당이 생겨서 그런지 금방 생각났다! 

무튼 저 긴 코드들은

```python
def solution(name):
    ...
        data  = find_next_index(index, count)
	...
    return answer

def find_next_index(idx, count):
    for num in range(len(count)):
        ascending, descending  = (num+idx)%len(count), (len(count)-num+idx) % len(count) # 1, 2, 3, 4 and 10, 9, 8, 7
        if count[ascending] != 0: return {"index":ascending, "move":num}
        if count[descending] != 0: return {"index":descending, "move":num}
```

완전 짧게 클린해짐! 


## 3. 스킬트리

##### 문제 요약

input 값의 알파벳 순서대로 다른 알파벳이 진행되는지 check 

##### 제한 조건

C → B → D 라면 CBD로 표기합니다
"CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2
##### 입출력 예 설명

- BACDE: B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트립니다.
- CBADF: 가능한 스킬트리입니다.
- AECB: 가능한 스킬트리입니다.
- BDA: B 스킬을 배우기 전에 C 스킬을 먼저 배워야 합니다. 불가능한 스킬트리입니다.


#### 내가 짠 코드 
```python
def solution(skill, skill_trees):
    count = 0
    for token in skill_trees:
        if check_right_skill_tree(token, skill):
            count += 1
    return count

def check_right_skill_tree(token, skill):
    stack = []
    for char in token:
        if char in skill:
            if skill.index(char) != len(stack):
                return False
            stack.append(char)
    return True
```

##### 알게된점 
다른사람 풀이 코드를 보니, for 는 else 를 제공해서, break 로 안짤린 경우에 else 가 실행된다함! 우와! 테스트 해서 고치려 해봤더니 잘 안되니... 


### 코드 리뷰
break 를 사용해서 처리하려했으나, 원하는 코드가 작성되지 않아 메서드를 따로 빼 false 처리를 했다.

하지만 지창이가 저번에 말했던 클린코드 중, 3번 이상 인덴트가 들어가는 부분에 고쳐야 한다는게 마음에 남는다. 개선해볼 필요가 있음!


## 4. 구명보트 

greedy 문제 
구명 보트에 몇명 타는가에 대한 문제

내가 짠 코드 -> 효율성 검사 에서 실패 
```python
def solution(people, limit):
    answer = 0
    people.sort()
    while(len(people) != 0):
        rest_weight = limit
        rest_weight -= people.pop()
        try: 
            if rest_weight >= people[0]: 
                del people[0]
        except: pass
        answer += 1
    return answer
```

##### 고친코드

```python
def solution(people, limit):
    answer = 0
    begin, end = 0, len(people)-1
    people.sort()
    while(start <= end):
        rest_weight = limit
        rest_weight -= people[end]
        end -=1 
        if rest_weight >= people[begin]: 
            start += 1
        answer += 1
    return answer
```

##### 다른사람들의 코드를 보고 개선한 코드

하..

```python
def solution(people, limit):
    answer = 0
    begin, end = 0, len(people)-1
    people.sort()
    while(begin <= end):
        if people[begin] + people[end] <= limit: 
            begin += 1
        end -= 1
        answer += 1
    return answer
```

#### 알게 된 점 

`del people[0]` 이 O(N)의 성능을 내기 떄문에 속도 면에서 - 를 먹었다. pop도 O(N)이었다! 그래서 index 비교로 변경해서 효율성 부분을 통과했다


## 5.다리를 지나는 트럭

<https://programmers.co.kr/learn/courses/30/lessons/42583>

여러분 도와주세여.. test case 5가 시간 초과가 뜹니다 ㅠㅡㅜ

```python
from collections import Counter, deque
def solution(bridge_length, weight, truck_weights):
    time= 0
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    truck_weights.reverse()  # nlogn 
    now = 0
    while(truck_weights): # n 
        next_truck = truck_weights[-1] 
        if sum(bridge) + next_truck <= weight: 
            bridge.append(next_truck) # O(1)
            truck_weights.pop() # O(1)
        else:
            bridge.append(0)
            if sum(bridge) + next_truck <= weight:
                bridge.pop()
                continue
        time += 1    
    return time + len(bridge)
```
고친코드

```python
# programmers lv2 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, max_weight, truck_weights):
    bridge = deque([0]*bridge_length, maxlen=bridge_length)
    bridge_current_weight = 0
    time = 0
    truck_weights.reverse()
    while truck_weights:
        time += 1
        next_truck = bridge.popleft()
        bridge_current_weight -= next_truck
        if bridge_current_weight + truck_weights[-1] > max_weight:
            bridge.append(0)            
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            bridge_current_weight += truck
    while bridge_current_weight > 0:
        time += 1
        next_truck = bridge.popleft()
        bridge_current_weight -= next_truck
    return time
```


## 6. 타겟 넘버

dfs 를 공부해야겠다 생각함

내가 짠 코드 
```python 
# programmers lv2 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165
# 별로인 내코드
from itertools import permutations, combinations
def solution(numbers, target):

    idx = []
    answer = 0
    for i in range(len(numbers)):
        idx.append(i)

    sumdata = sum(numbers)
    for i in range(len(numbers)+1):
        combination = [list(number) for number in combinations(idx, i)]
        for minuslist in combination:
            minusdata = 0
            for number in minuslist:
                minusdata += numbers[number] 
            if (sumdata - (minusdata * 2)) == target:
                answer += 1
    return answer
```

깔끔 recursive code

```python
def solution(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0]) 
```

## 7. 주식 가격 

stack 관련 문제라는데, 이렇게 풀었당. 비슷한 코드에서 스택을 구현한거보다 이게 2배 느리다는데 왤까..?
```python
# programmes lv2. 주식가격 
# https://programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    size = len(prices)
    prices = deque(prices)
    answer = []
    while(prices):
        count = 0
        current_price = prices.popleft()
        for next_price in prices:
            if current_price <= next_price:
                count +=1
            else:
                count +=1
                break
        answer.append(count)
    return answer
```



## 8. 쇠 막대기

![쇠막대기](https://grepp-programmers.s3.amazonaws.com/files/ybm/dbd166625b/d3ae656b-bb7b-421c-9f74-fa9ea800b860.png)

()가 만났을때, 양쪽 인덱스 차이가 _-1_ 일경우, 레이저가 된다. 이때는 레이저에서 잘린 왼쪽스틱의 값이 발생한다. 

아닐경우, 스틱이 끝나는 지점이 되는데, 오른쪽 잘린 스틱 +1 값을 더해준다.

내가 짠 코드

```python
# programmers lv2 쇠막대기
# https://programmers.co.kr/learn/courses/30/lessons/42585
def solution(arrangement):
    answer = 0
    stick = []
    for idx, value in enumerate(arrangement): # O(N)
        if value == "(": 
            stick.append(idx)
        if stick and value == ")":
            right, left = idx, stick.pop()
            if right - left == 1: 
                answer += len(stick)
            else: 
                answer += 1
    return answer
```





## 9. 정수 삼각형

![img](https://grepp-programmers.s3.amazonaws.com/files/production/97ec02cc39/296a0863-a418-431d-9e8c-e57f7a9722ac.png)

숫자를 좌우로내려가면서 나오는 최대값이 뭔지 리턴하면됨. 

처음에는 재귀를 썼다. 위에서 아래 내려가면서 max 값을 체크하면서 풀었으나.. 시간 초과됨 ㅠㅡㅠ

내가 짠 코드 

```python
from collections import deque

def solution(triangle):
    for col in range(1, len(triangle)):
        for row in range(len(triangle[col])):
            
            if row == 0: 
                triangle[col][row] += triangle[col-1][row]
            elif row+1 == len(triangle[col]):
                triangle[col][row] += triangle[col-1][row-1]
            else:
                triangle[col][row] += max(triangle[col-1][row], triangle[col-1][row-1])
    return max(triangle[-1])
```

대박 코드 한줄!

```python
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
```


## 10. 기능 개발

개발이 완료되서 출시하는 값의 갯수를 리턴하면됨. 
근데 순차적으로 되야해서

progresses	speeds	return
[93,30,55]	[1,30,5]	[2,1]
이렇게 들어왔을때 

93 은 하루에 1퍼 씩 완성 되니까 7일이걸리고, 30 은 하루에 30퍼씩 완성 되니까 4일이 걸리는데, 첫번째 작업이 완성되지않아 기다렸다가 같이 출시를 해주는거.

#### 내가 짠 코드 

```python
#!/bin/python3
import pytest

@pytest.mark.parametrize("progresses, speeds, expected", [
    ([93,30,55],[1,30,5],[2,1]),
    ([93, 30, 55, 60, 40, 65], [1, 30, 5 , 10, 60, 7], [2,4]),
    ([40, 93, 30, 55, 60, 65], [60, 1, 30, 5 , 10, 7], [1, 2, 3]),
])


def test_simple(progresses, speeds, expected):
    assert solution(progresses, speeds) == expected

COMPLETE = 100
def solution(progresses, speeds):
    answer = []
    complete_days = []
    for i,progress in enumerate(progresses):
        days = (COMPLETE - progress) // speeds[i]
        if (COMPLETE - progress) % speeds[i] > 0: days += 1
        complete_days.append(days)
    
    flag, count = 0, 0
    for i,v in enumerate(complete_days):
        if i == 0:
            flag = complete_days[i]
            continue
        if complete_days[i] <= flag: count += 1
        else:
            answer.append(count+1)
            flag = complete_days[i]
            count = 0
    answer.append(count+1)
    return answer
```

잘짰다고 생각한 다른사람 풀이. 명확한 것 같다.

```python
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
```