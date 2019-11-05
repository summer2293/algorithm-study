# Heap 발표 자료 준비
## 우선순위 큐
	- 일반 스택과 큐와 비슷한 추상 데이터 타입이지만, 각 항목마다 연관된 우선순위가 있음
	- 두 항목의 우선순위가 같으면 큐의 순서를 따름 (FIFO)
	- 힙을 이용해서 구현

## Heap
- 각 노드가 하위 노드보다 작은(또는 큰) 이진 트리
- 균형 트리의 모양이 수정될 떄, 이를 다시 균형 트리로 만드는 시간 복잡도:  `O(log n)`
- 리스트에서 가장 작은(혹은 가장 큰) 요소에 반복적으로 접근하는 프로그램에 유용함
- 최소(최대)힙 사용시 가장 작은(큰) 요소를 처리하는 시간 복잡도가 -> `O(1)`
	- 그 외 조회, 추가, 수정을 처리하는 시간복잡도는 `O(log n)`

## Python heaps 모듈
```python
>>> import heapq
>>> list1 = [4, 6, 8, 1]
>>> heapq.heapify(list1)
>>> list1
>>> [1, 4, 8, 6]
```

- 항목 삽입시 -> `heapq.heappush(heap, item)`
```python
h = []
heapq.heappush(h, (1, 'a'))
heapq.heappush(h, (2, 'lala'))
heapq.heappush(h, (3, 'temp'))
print(h)
---
>>> [(1, 'a'), (2, 'lala'), (3, 'temp')]
```

- 가장 작은 항목 제거 및 반환 -> `heapq.heappop`
```python
heapq.heappop(h)
>>> [(2, 'lala'), (3, 'temp')]
```

- `heaps.heappushpop(heap, item)`  새 항목에 힙 추가후 가장 작은 항목 제거하고 반환
- `heap.heapreplace(heap, item` 은 힙의 가장 작은 항목을 제거하고 반환한 후, 새 항목을 추가
- `heappush()` 와 `heappop()` 메서드를 따로 사용하는것보다 위 메소드를 사용하는 것이 더 효율적
- `heapq.merge(*iterables)` 여러 개의 정렬된 반복 가능한 객체를 병합하여 하나의 정렬된 결과의 이터레이터를 반환
```python
for x in heapq.merge([1, 3, 5], [2, 4, 6]):
    print(x)
---
1
2
3
4
5
6
``` 

## 최대 힙 구현하기
```python
class Heapify(object):
    def __init__(self, data):
        self.data = data or []
        for i in range(len(data) // 2, -1, -1):
            self.__max_heapify__(i)

    def __repr__(self):
        return repr(self.data)

    def parent(self, i):
        if i & 1:
            return i >> 1
        else:
            return (i >> 1) - 1

    def left_child(self, i):
        return (i << 1) + 1

    def right_child(self, i):
        return (i << 1) + 2

    def __max_heapify__(self, i):
        largest = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.data)

        # 왼쪽 자식
        largest = (left < n and self.data[left]) > self.data[i] and left or i

        # 오른쪽 자식
        largest = (right < n and self.data[right]) > self.data[largest] and right or largest
        import ipdb; ipdb.set_trace()

        # 현재 노드가 자식들보다 크다면 Skip, 자식이 크다면 Swap
        if i is not largest:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            # print
            self.__max_heapify__(largest)

    def extract_max(self):
        n = len(self.data)
        max_element = self.data[0]

        # 첫 번째 노드에 마지막 노드를 삽입
        self.data[0] = self.data[n - 1]
        self.data = self.data[:n - 1]
        self.__max_heapify__(0)
        return max_element

    def insert(self, item):
        i = len(self.data)
        self.data.append(item)
        while (i != 0) and item > self.data[self.parent(i)]:
            print(self.data)
            self.data[i] = self.data[self.parent(i)]
            i = self.parent(i)
        self.data[i] = item


if __name__ == '__main__':
    l1 = [3, 2, 5, 1, 7, 8, 2]
    h = Heapify(l1)
    print(h)
    assert h.extract_max() == 8
```


## 우선순위 큐 구현하기
```python
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({0!r})".format(self.name)


if __name__ == '__main__':
    """ push와 pop 은 모두 O(logN)이다. """
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    assert str(q.pop()) == "Item('test2')"
    assert str(q.pop()) == "Item('test3')"

```
