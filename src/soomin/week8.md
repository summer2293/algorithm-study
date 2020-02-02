## week8

#### 오픈 채팅방(<https://programmers.co.kr/learn/courses/30/lessons/42888>)

```python
def solution(record):
    user = dict()
    tokens = []
    answer = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}


    # part token O(N)
    for timeline in record: 
        tokens.append(timeline.split(" "))

    # user uid setting O(N)
    for token in tokens:
        try: user[token[1]] = token[2]
        except: pass

    # print message  O(N) 
    for token in tokens:
        action = token[0]
        name = token[1]
        message = ""
        if action == "Enter":
            message += "{nickname}님이 들어왔습니다.".format(nickname=user[name])
        elif action == "Leave":
            message += "{nickname}님이 나갔습니다.".format(nickname=user[name])
        else: continue
        answer.append(message)
    return answer
```
다른사람 풀이 보고 개선해본 코드
```python
# 개선 코드 (다른사람 풀이 보고 )
def solution(record):
    user = dict()
    answer = []
    tokens = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    # user setting O(N)
    for timeline in record: 
        token = timeline.split(" ")
        try: user[token[1]] = token[2]
        except: pass
        tokens.append(token)

    # print message  O(N) 
    for token in tokens:
        action, name = token[0], token[1]
        message = ""
        try: message += user[name] + messages[action]
        except: continue
        answer.append(message)
    return answer
```



#### 멀쩡한 사각형(<https://programmers.co.kr/learn/courses/30/lessons/62048>)

```python
# 예전에 풀어본 적 있어서 품. 원리는 모르겠음 누가 알랴주세요
def solution(w,h):
    answer = 0
    short, long = min(w,h), max(w,h) # O(N)
    while (short != 0): 
        if short == 1: return answer # 짧은 길이가 1이 될 경우 return 
        count = long//short
        long %= short
        answer += ((short ** 2) - short) * count         
        short, long = min(short,long), max(short,long) # swap
    return answer
```



#### 괄호 변환

```python
def solution(p):
    answer = ''
    
    # 1. 빈문자 or 올바른 문자 check()
    if correct(p) is True: return p
    
    # 2. 올바른 u
    u, v = p[:balance(p)],  p[balance(p):]
    if correct(u): 
        return u + solution(v)
    
    # 올바르지 않은 u
    answer = "(" + solution(v) + ")"
    for char in list(u)[1:-1]:
        if char == "(":
            answer += ")"
        else: 
            answer += "("
    return answer


def correct(p):
    left, right = 0, 0
    for char in p:
        if char == "(": 
            left += 1
        else: 
            if left != 0: left -= 1
            else: right += 1
    if left == right == 0: return True

def balance(p):
    count = 0
    for idx, char in enumerate(p):
        count = count-1 if char == "(" else count+ 1
        if count == 0: return idx + 1
```

답 보고 개선해본 코드 

```python
def solution(p):
    if correct(p) is True: return p 
    idx = balance(p) + 1
    u, v = p[:idx],  p[idx:]
    if correct(u): return u + solution(v)
    else: return "(" + solution(v) + ")" + swap(list(u)[1:-1]) 

# left, right 변수 1개로 변경 
def correct(p):
    count = 0 
    for char in p:
        if char == "(": count += 1
        else: count -= 1
        if count < 0: return False
    return True


def balance(p):
    count = 0
    for idx, char in enumerate(p):
        count = count-1 if char == "(" else count+ 1
        if count == 0: return idx

def swap(u):
    answer = ''
    for char in u:
        if char == "(": answer += ")"
        else: answer += "("
    return answer
```



#### 124 나라

어려워서 코드 검색 ㅠㅡㅠ 개쩐다고 생각한 코드 
```python
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return int(answer)
```



## 개별문제

### 캐시

##### 문제 

DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

##### 입력 형식

- 캐시 크기(`cacheSize`)와 도시이름 배열(`cities`)을 입력받는다.
- `cacheSize`는 정수이며, 범위는 0 ≦ `cacheSize` ≦ 30 이다.
- `cities`는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
- 각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

##### 출력 형식

- 입력된 도시이름 배열을 순서대로 처리할 때, 총 실행시간을 출력한다.

##### 조건

- ##### 캐시 교체 알고리즘은 `LRU`(Least Recently Used)를 사용한다.

- `cache hit`일 경우 실행시간은 `1`이다.

- `cache miss`일 경우 실행시간은 `5`이다.

##### 입출력 예제

| 캐시크기(cacheSize) | 도시이름(cities)                                             | 실행시간 |
| ------------------- | ------------------------------------------------------------ | -------- |
| 3                   | [Jeju, Pangyo, Seoul, NewYork, LA, Jeju, Pangyo, Seoul, NewYork, LA] | 50       |
| 3                   | [Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul, Jeju, Pangyo, Seoul] | 21       |
| 2                   | [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome] | 60       |
| 5                   | [Jeju, Pangyo, Seoul, NewYork, LA, SanFrancisco, Seoul, Rome, Paris, Jeju, NewYork, Rome] | 52       |
| 2                   | [Jeju, Pangyo, NewYork, newyork]                             | 16       |
| 0                   | [Jeju, Pangyo, Seoul, NewYork, LA]                           | 25       |

### LRU 

![image](https://www.researchgate.net/profile/Gyanendra_Kumar12/publication/319467661/figure/fig2/AS:536152847417344@1504840208056/LRU-page-replacement-algorithm-with-3-memory-frames.png>)

- 페이지 교체 알고리즘 (TMI. FIFO 도 페이지 교체 알고리즘 중 하나이다)

- 컴퓨터에 램이 속도가 빠르기 때문에, 램에 블록을 만들어 데이터를 저장한다. 이 블록을 같은 크기로 생성하는데 이걸 "페이지" 라고한다.
- CPU 가 계산을 할때 필요한 데이터가 "페이지" 에있다면 _cache_hit_ 라고 부르고, 없다면 _cache_miss_ 라고 부른다.  

- _cache_hit_ 가 발생하면 조회 된 값을 가장 최신 상태로 옮긴다.
- _cache_miss_ 가 발생하면 가장 오래된 값을 빼고 새로운 값을 최신 상태에 넣는다.



### 코드

```python
from collections import deque
CACHE_HIT = 1
CACHE_MISS = 5
def solution(cacheSize, cities):
    if not cacheSize: 
        return len(cities) * 5 # cache 0 > runtime = cities * 5
    
    runtime, memory = 0, deque(maxlen=cacheSize)
    
    for city in cities:
        city = city.lower()
        
        if city in memory: 
            memory.remove(city) 
            runtime += CACHE_HIT
        else: 
            runtime += CACHE_MISS
        
        memory.append(city) 
    return runtime
```

### 고려한점

##### deque 사용

list 의 경우 size 조절이 안되나, deque 는 `maxlen` 이 존재해서 이 이후의 값을 받지 않아 편했다. 그리고 메모리 값을 계속 swap 해야하는 경우에 deque 가 list 보다 더 효율적이라고 생각함!  이부분이 아니라면 코드리뷰 꼭 부탁합니당. 자신이없셔요..!

###### deque remove method

그리고 `remove` 메서드를 몰라 처음에는, `del memory(memory.index(city))` 로 했는데 이런것이있었다니! 나처럼 모르는 사람 있다면 알고가세융

##### 변수이름 고려

원래 deque()  를 선언한 이름이 `cache` 였는데, `cacheSize` 의 비슷한 이름이 있기도하고, `memory` 가 더 잘 와닿는 것 같아서 바꿨다.

##### 짧은 코드 

>  사실 이게 더 잘 읽히는 코드인지는 모르겠음.! 이부분에 대한 의견을 바랍니다 
>
> ```python
> if city in memory: # memory 값이 있을 경우 최신 값으로 swap 
> 	memory.remove(city) 
>     memory.append(city)
> 	runtime += 1
> else: # memory 값이 없을 경우 append
>     runtime += 5 
> 	memory.append(city) 
> ```

이 부분에서, `memory.append(city) ` 가 중복 되는것 같아 아래로 뺐음!

> ```python
> if city in memory: # memory 값이 있을 경우 최신 값으로 swap  
> 	memory.remove(city) 
> 	runtime += 1
> else: runtime += 5 
> 
> memory.append(city) 
> ```
>
> 중복을 제거하는게 좋긴 한데,  if / else 랑 있을 때 이 안에서 뭔 일이 일어나는지 정확히 어떤 코드인지는 알 수가 없는 것 같아서. 중복을 제거하는것이 좋은가, 명확한 코드가 좋은가에 대한 궁금함이 생겼다! 
>
> > 개발자들은 반복되는 코드보면 미쳐버리기 때문에 아래 값이 좋다는 소리를 들었다



