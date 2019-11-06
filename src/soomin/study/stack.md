## Stack

__Last In Out First__ 방식을 가지고 있는 데이터 저장 방법. 자료가 순서대로 저장되며, 마지막에 들어온 데이터가 먼저 나가는 방법을 말한다. 일상 생활에서 책을 꺼내거나, 웹서핑 후 뒤로가기를 누를 때 스택이 사용된다.

![Stack Structure](https://miro.medium.com/max/1760/1*S2ujFRrOU_GJQOhhQD8LyA.png)



## 기능

- `push`: 데이터를 넣는 기능. 가장 위 (`top`) 에서 데이터를 추가한다.
- `pop`: 데이터를 뽑는 기능. 가장 위 (`top`) 에서 데이터를 제거한다.
- `top`: 제일 위를 가르키고 있는 포인터. `push` `top` 둘 다 `top` 에 있는 데이터만 뽑을 수 있다.
- `peek`: 스택의 가장 위 데이터의 내용을 반환한다.
- `is empty`: 스택이 비어있을 경우 `true` 를 반환한다. 

## 특징

- 가장 위 데이터만 알 수 있다. 
- 문제의 종류에 따라 배열보다 스택에 데이터를 저장하는 것이 더 적합한 방법일 수 있다.

## 사용 사례

- 재귀 알고리즘
- 웹 브라우저 방문 기록
- 실행취소
- 역순 문자열 만들기
- 수식 괄호 검사
- 후위 표기법 계산 

## 스택 구현

python docs 에서는 __리스트__ 를 이용해 스택을 구현한다. python 의 리스트는 __동적 배열__ 이기 때문에 새로운 원소를 _삽입_, _삭제_ 할 수 있다. List 변수에는 첫번째 원소값 주소가 저장되기 때문에, 마지막 원소의 데이터 또한 불러올 수 있다. 

```python
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, e):
        self.stack.append(e)
    
    def pop(self):
        if self.stack: return self.stack.pop() 

    def isEmpty(self):
        return self.stack if True else False

    def peek(self):
        if self.stack: return self.stack[-1]

```

## 시간복잡도

- __O(1)__

  - pop
  - push
  - is_empty
  - peek

  pop / push 의 경우 평균이 1이다. pop 은 마지막 성분을 뽑는다. 

python __list__ 의 경우 `pop`,`append` 기능을 가지고 있기 때문에 스택을 대체하지만, list는 resize 를 __growth pattern__ 을 두고 list size 를 재할당한다. 이럴경우 array size 초과시 2n 사이즈 재할당이 일어나기 때문에 이 때 시간복잡도는 __O(N)__ 이 된다. 이게 시르면 디큐로하면됨 
