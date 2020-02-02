### week8

#### 오픈채팅방

```python
def solution(record):
    answer = []

    dict = {}

    for i in range(len(record)):
        if record[i][0] != 'L' :
            x,y,z = record[i].split(' ')
            dict[y] = z

    for i in range(len(record)):
        if record[i][0] == 'E':
            x,y,z = record[i].split(' ')
            answer.append(dict[y]+'님이 들어왔습니다.')
        elif record[i][0] == 'L' :
            x, y = record[i].split(' ')
            answer.append(dict[y]+'님이 나갔습니다.')

    return answer
```

#### 멀정한 사각형

```python
def solution(w,h):
    if(w == h):
        return w*h-w
    else :
        a = w
        b = h
        # 최대 공약수 구하는부분 start
        if b>a:
            tmp = a
            a = b
            b = tmp
        while b>0:
            c = b
            b = a % b
            a = c
        # end
        return w*h - (w+h-a)
```

#### 괄호변경

#### 이전 개선코드

```python
# 문제 이해하고 다시 풀엇지만 실패...
def solution(p):
    answer = ''
    v = ''
    if p == '' :
        return p

    left_count = 0
    right_count = 0
    check = True

    for i in range(len(p)):
        if p[i] == '(':
            left_count +=1
            answer += p[i]

        else :
            right_count +=1
            answer += p[i]
            if right_count > left_count :
                check = False
        if left_count == right_count:
            if check == True :
                return answer + solution(p[i+1:])
            else :

                return '(' + solution(p[i+1:]) + ')' + answer[1:-1][::-1]

    return answer
```

#### 실패코드

```python
# 문제 이해를 잘 못해서 틀림
def solution(p):
    answer = ''
    v = ''
    if p == '' :
        return p

    left_count = 0
    right_count = 0
    check = True

    for i in range(len(p)):
        if p[i] == '(':
            left_count +=1
            answer += p[i]

        else :
            right_count +=1
            answer += p[i]
            if right_count > left_count :
                check = False
        if left_count == right_count:
            if check == True :
                return answer + solution(p[i+1:])
            else :
                front = answer[0]
                answer = answer[1:]
                end = answer[-1]
                answer = answer[:-1]
                answer = answer[::-1]
                answer = end + answer + front
                return answer + solution(p[i+1:])

    return answer
```

#### 124 나라의 숫자

```python
# 3진법이여서 3으로 나누는거까지는 생각했는데 1을 빼야 되는거는 생각을 못했네요ㅜㅜ
# 2시간 고민하다가 못풀겠어서 다른사람 풀이 봤습니다... 1을 빼야하는거는 아직 이해가 안가네요..
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
```

## 보너스 문제

### 주식가격

```python
def solution(prices):
    answer = []
    for i in range(len(prices)):
        num = 1
        for j in range(i+1, len(prices)-1):
            if(prices[i] <= prices[j]):
                num+=1
            else:
                break
        answer.append(num)
        num = 0
    answer[-1] = 0
    return answer

```

## 개별문제

### 탑

> 수평 직선에 탑 N대를 세웠습니다. 모든 탑의 꼭대기에는 신호를 송/수신하는 장치를 설치했습니다. 발사한 신호는 신호를 보낸 탑보다 높은 탑에서만 수신합니다. 또한, 한 번 수신된 신호는 다른 탑으로 송신되지 않습니다.

> 예를 들어 높이가 6, 9, 5, 7, 4인 다섯 탑이 왼쪽으로 동시에 레이저 신호를 발사합니다. 그러면, 탑은 다음과 같이 신호를 주고받습니다. 높이가 4인 다섯 번째 탑에서 발사한 신호는 높이가 7인 네 번째 탑이 수신하고, 높이가 7인 네 번째 탑의 신호는 높이가 9인 두 번째 탑이, 높이가 5인 세 번째 탑의 신호도 높이가 9인 두 번째 탑이 수신합니다. 높이가 9인 두 번째 탑과 높이가 6인 첫 번째 탑이 보낸 레이저 신호는 어떤 탑에서도 수신할 수 없습니다.

| 송신 탑(높이) | 수신 탑(높이) |
| ------------- | ------------- |
| 5(4)          | 4(7)          |
| 4(7)          | 2(9)          |
| 3(5)          | 2(9)          |
| 2(9)          | -             |
| 1(6)          | -             |

> 맨 왼쪽부터 순서대로 탑의 높이를 담은 배열 heights가 매개변수로 주어질 때 각 탑이 쏜 신호를 어느 탑에서 받았는지 기록한 배열을 return 하도록 solution 함수를 작성해주세요.

##### 제한 사항

- heights는 길이 2 이상 100 이하인 정수 배열입니다.
- 모든 탑의 높이는 1 이상 100 이하입니다.
- 신호를 수신하는 탑이 없으면 0으로 표시합니다.

##### 입출력 예 설명

| heights         | return          |
| --------------- | --------------- |
| [6,9,5,7,4]     | [0,0,2,2,4]     |
| [3,9,9,3,5,7,2] | [0,0,0,3,3,3,6] |
| [1,5,3,6,7,6,5] | [0,0,2,0,0,5,6] |

입출력 예 #1
앞서 설명한 예와 같습니다.

입출력 예 #2

[1,2,3] 번째 탑이 쏜 신호는 아무도 수신하지 않습니다.
[4,5,6] 번째 탑이 쏜 신호는 3번째 탑이 수신합니다.
[7] 번째 탑이 쏜 신호는 6번째 탑이 수신합니다.

입출력 예 #3

[1,2,4,5] 번째 탑이 쏜 신호는 아무도 수신하지 않습니다.
[3] 번째 탑이 쏜 신호는 2번째 탑이 수신합니다.
[6] 번째 탑이 쏜 신호는 5번째 탑이 수신합니다.
[7] 번째 탑이 쏜 신호는 6번째 탑이 수신합니다.

#### 접근 방식

> 왼쪽에서부터 오른쪽으로 높이가 큰 탑의 위치를 반환한다. 일단 배열을 리턴에서 0번째부터 순서대로 돌아가게했다. 그리고 처음값과 다음값을 비교해서 다음값이 크면 그위치를 배열에 넣고 작으면 다음 값으로 넘어간다. 계속반복한다.

````python
def solution(heights):
    heights = heights[::-1]
    length = len(heights)
    check = False
    answer = []

    for i in range(len(heights)):
        for j in range(i, len(heights)-1):
            if heights[i] < heights[j+1]:
                answer.append(length-j-1)
                check = True
                break
        if check == False:
            answer.append(0)
        else :
            check = False



    return answer[::-1]
    ```
````
