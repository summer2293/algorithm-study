# STACK

> _by JichangJang, https://github.com/jangjichang_ 

### 개념 설명

먼저, 스택입니다. 스택은 LIFO(Last In First Out)순서를 따르는 선형 데이터 구조입니다. 스택의 모든 삭제 및 삽입은 스택 상단에서 수행됩니다. 그래서 마지막으로 추가된 요소가 스택에서 가장 먼저 제거됩니다. 이것이 LIFO라고 불립니다.

![stack](https://github.com/jangjichang/Today-I-Learn/blob/master/Algorithm/theory/stack.jpg?raw=true)

### 연산

- push: 스택에 새로운 요소를 추가합니다.
- pop: 스택에서 요소를 제거합니다.
- isEmpty: 스택이 비어있는지 확인합니다.
- peek: 스택의 맨 위 요소를 반환합니다.



### 구현

그렇다면 스택을 어떻게 구현할까요? python tutorial 공식 문서의 [리스트를 스택으로 사용하기](https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-stacks)를 살펴보겠습니다.

스택에 새로운 요소를 추가할 경우 append()를 사용하고 스택에서 요소를 제거할 경우 명시적인 인덱스 없이 pop()을 사용하라고 하네요. 예시를 참고해서 Stack Class를 만들면 아래와 같습니다.

```python
class Stack():
    def __init__(self):
        self.stack = list()

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def isEmpty(self):
        if self.stack:
            return False
        return True

    def peek(self):
        if self.stack:
            return self.stack[-1]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.peek())
    print(s.isEmpty())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.isEmpty())
```



### 관련 문제

- https://leetcode.com/problems/min-stack/
- https://leetcode.com/problems/valid-parentheses/



### 참고
- https://docs.python.org/ko/3/tutorial/datastructures.html#using-lists-as-stacks
- https://techdifferences.com/difference-between-stack-and-queue.html