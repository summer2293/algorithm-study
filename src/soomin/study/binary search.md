## Binary Search

정렬한 자료를 반으로 나누어 탐색하는 기법. 

- 자료는 정렬되어 있어야 한다. 
- 로그 실행 시간을 보장한다. 



#### 구성 요소

- __target__ : 찾고자 하는 값
- __data__: 정렬된 list
- __start__ : 첫 index
- __end__: 끝 index
- __mid__ : start, end 의 중간 값



#### 방법

1. mid index value 를 찾는다
2. target 과 mid 가 같은지 체크
3. 없다면 대 소 비교하여 절반을 자른다. 
4. 동일연산 반복



#### python 구현 (recursive)

```python
def binary_search(target, start, end, data):
    if start > end:
        return None
    
    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    
    if data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        
        
    return binary_search_recursion(target, start, end, data)
```



#### 시간복잡도

시간 복잡도는 BigO 표기법으로 O(logN) 으로 나타낼 수 있다.



## Binary Search Tree

#### 특징

- binary search + linked list 구조

- linked list 는 삽입이 O(1) 이지만, 탐색이 O(N) 의 복잡성이 발생한다. 이를 해결하기 위해 이진 탐색 트리가 고안되었다.

- 중위 순회 방식을 사용한다.

- __부모노드가 왼쪽 자식노드보다 크거나 같고, 오른쪽 자식노드보다 작거나 같다__



## Heap vs BST

##### 공통점

- 이진트리

##### 차이점

노드값이 다르게 구성된다

- 힙

  부모 > 자식 노드. 우선순위 정렬에 강점.

- BST

  왼쪽 자식 노드 < 부모 < 오른쪽 자식 노드. 탐색에 강점 



