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

