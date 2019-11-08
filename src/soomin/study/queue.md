## Queue

__FIFO (First In First Out)__ 방식을 가지는 데이터 저장방법. 

![queue](https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Data_Queue.svg/1200px-Data_Queue.svg.png)

따라서 자료의 삽입 / 삭제 위치가 다르다. 

## 기능

- `enqueue` : 큐에 요소를 추가한다
- ` dequeue` : 큐에서 요소를 제거한다
- `peek` : 큐의 맨 위 요소를 반환한다. 
- `is_empty` : 큐가 비어있는지 확인한다. 



## 특징

- 삽입과 삭제만 존재한다.
- 오버워치 / 롤에서 큐를 들어봤다면 그 큐가 이 큐다 



##### 시간 복잡도

__O(1)__ - enque / deque



## 큐 구현

```python
from collections import deque

class Queue:
    def __init__(self, value=list()):
        self.queue = deque(value)
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        self.queue.popleft()

    def peek(self):
        if self.queue:
            return self.queue[-1]
    
    def isempty(self):
        if self.queue:
            return False
        return True
```
