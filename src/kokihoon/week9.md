### week9

#### 단어변환

```python
# 너무 어려워서 다른사람꺼 풀이 참고했스니다.!!
def solution(begin, target, words):
    answer = 0

    if target not in set(words):
        return 0

    list_word = [begin]

    while len(words) != 0:
        for value in list_word:
            temp = []
            for word in words:
                count = 0
                for index in range(len(word)):
                    if value[index] != word[index]:
                        count+=1
                    if count == 2:
                        break
                if count == 1:
                    temp.append(word)
                    words.remove(word)

        answer += 1
        if target == "".join(temp):
            return answer
        else:
            list_word = temp

    return answer
```

#### 베스트 앨범

```python
## 결국 실패했네요ㅜㅜ
def solution(genres, plays):
    answer = []
    set_dict = {}
    list_1 = []
    for i,(x, y) in  enumerate(zip(genres, plays)):
        list_1.append((i,x, y))
        if x in set_dict:
            set_dict[x] += y
        else:
            set_dict[x] = y

    sdict= sorted(set_dict.items(), reverse=True) # 합의 최대값 순으로 정렬
    list_1 = sorted(list_1, key = lambda x: (x[1], -x[2]))

    check = 0
    for x, y in sdict:
        for x1,y1,z1 in list_1:
            print(x1, y1, z1)
            if x == y1:
                answer.append(x1)
                check += 1

            if check == 2 or (check == 1 and y1 != x):
                check = 0
                break

    return answer
```

#### N-Queen

```python
## 너무 어려워요..ㅜㅜ
```

## 개별문제

### 여행 경로

#### 문제 설명

> 주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 ICN 공항에서 출발합니다.

> 항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##### 제한사항

- 모든 공항은 알파벳 대문자 3글자로 이루어집니다.
- 주어진 공항 수는 3개 이상 10,000개 이하입니다.
- tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
- 주어진 항공권은 모두 사용해야 합니다.
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
- 모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

##### 입출력 예

| tickets                  | return               |
| ------------------------ | -------------------- |
| [[ICN, JFK],             | [HND, IAD],          |
| [JFK, HND]]              | [ICN, JFK, HND,      | IAD] |
| [[ICN, SFO], [ICN, ATL], | [ICN, ATL, ICN, SFO, |
| [SFO, ATL], [ATL, ICN],  | ATL, SFO]            |
| [ATL,SFO]]               |                      |

입출력 예 설명
예제 #1

[ICN, JFK, HND, IAD] 순으로 방문할 수 있습니다.

예제 #2

[ICN, SFO, ATL, ICN, ATL, SFO] 순으로 방문할 수도 있지만 [ICN, ATL, ICN, SFO, ATL, SFO] 가 알파벳 순으로 앞섭니다.

#### 접근 방식

>

```python

```
