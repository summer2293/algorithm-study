# SORT(정렬)

> _by KunhoKim, <https://github.com/kimkunho980422>_



## 개념 
정렬 알고리즘은 n개의 숫자가 입력으로 주어졌을 때, 이를 사용자가 지정한 기준에 맞게 정렬하여 출력하는 알고리즘이다.
예를 들어, 숫자의 오름차순 & 내림차순, 문자의 사전적 정렬 등이 있다.

파이썬에는 `list`에서 원소를 오름차순으로 정렬해주는 `sort()`라는 내장함수가 존재한다(in-place method).
이는 합병 정렬과 삽입 정렬의 영향을 받은 [Tim 정렬 알고리즘](https://en.wikipedia.org/wiki/Timsort)을 사용하고 있다.

또한, list를 포함한 다른 `iterable(dictionary, string, tuple etc..)`에서 정렬해주는 `sorted()`라는 내장함수도 존재한다. list를 제외한 iterable에서는 sort()를 사용할 수 없다.(AttributeError)

```python
# sort의 사용법(오름차순 정렬): 기존 배열의 순서를 바꾼다. None을 반환한다.
>>> a = [1, 10, 5, 7, 6]
>>> a.sort()
>>> a
[1, 5, 6, 7, 10]

# sort의 사용법(내림차순 정렬): 기존 배열의 순서를 바꾼다. None을 반환한다.
>>> a = [1, 10, 5, 7, 6]
>>> a.sort(reverse=True)
>>> a
[10, 7, 6, 5, 1]

# 위와 동일한 내림차순의 결과를 얻을 수 있는 reverse: 기존 배열의 순서를 바꾼다.
>>> a = [1, 10, 5, 7, 6]
>>> a.sort()
>>> a.reverse()
>>> a
[10, 7, 6, 5, 1]

# sorted의 사용법(오름차순 정렬): 기존 리스트의 순서를 바꾸지 않고 새로운 리스트를 반환한다.
>>> a = [1, 10, 5, 7, 6]
>>> b = sorted(a)
>>> a
[1, 10, 5, 7, 6]
>>> b
[1, 5, 6, 7, 10]

# sorted의 사용법(내림차순 정렬): 기존 리스트의 순서를 바꾸지 않고 새로운 리스트를 반환한다.
>>> a = [1, 10, 5, 7, 6]
>>> b = sorted(a, reverse=True)
>>> a
[1, 10, 5, 7, 6]
>>> b
[10, 7, 6, 5, 1]

# 위와 동일한 내림차순의 결과를 얻을 수 있는 reversed: reversed()는 iterable한 객체를 반환하기 때문에 list형태로 한 번 더 변형이 필요하다.
>>> a = [1, 10, 5, 7, 6]
>>> b = list(reversed(sorted(a)))
>>> a
[1, 10, 5, 7, 6]
>>> b
[10, 7, 6, 5, 1]

# list가 아닌 iterable에서 sorted의 사용법(오름차순 정렬)
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```


## Selection Sort(선택 정렬)
선택 정렬은 이름에 맞게 현재 위치에 들어갈 값을 찾아 정렬하는 알고리즘이다. 현재 위치에 저장될 값의 크기가 작냐, 크냐에 따라 최소 선택 정렬(Min-selection sort)와 최대 선택 정렬(Max-seletion sort)로 구분할 수 있다.
최소 선택 정렬은 오름차순, 최대 선택 정렬은 내림차순으로 정렬된다. 알고리즘은 다음과 같다.

1. 주어진 배열에서 최소값 혹은 최대값을 찾는다.
2. 그 값을 맨 앞에 위치한 값과 교체한다.
3. 맨 처음 위치를 뺀 나머지 배열을 같은 방법으로 교체한다.
4. 하나의 원소만 남을 때까지 위의 방법을 반복한다.

`시간 복잡도`는 배열에서 n, n-1, n-2, ..., 2, 1개의 원소에 대해 전체 비교를 진행하므로 `O(n^2)`이다. 

```python
def MinSelectionSort(List): #오름차순
    for size in range(len(List)):
        min = 0
        for i in range(1, size):
            if List[i] > List[min]:
                min = i
        List[min], List[size] = List[size], List[min] 
```

## Insertion Sort(삽입 정렬)
삽입 정렬은 현재 위치에서 그 이하 배열들을 비교한 후, 자신이 들어갈 위치를 찾아 그 위치에 삽입하는 정렬 알고리즘이다. 알고리즘은 다음과 같다.

1. 배열의 두번째 인덱스부터 시작하여, 현재 인덱스의 값은 별도의 변수에 저장해주고 비교 인덱스를 현재 인덱스-1로 잡는다.
2. 별도로 저장해 둔 변수(삽입 변수)와 비교 인덱스의 값을 비교한다.
3. 삽입 변수의 값이 더 작으면, 현재 인덱스로 비교 인덱스의 값을 저장해주고 비교 인덱스를 -1하여 비교를 반복한다.
4. 삽입 변수의 값이 더 크면, 비교 인덱스+1에 삽입 변수를 저장한다.

`시간 복잡도`는 `최악의 경우(배열이 역정렬 되어 있을 때)` n-1, n-2, ..., 2, 1개의 원소에 대해 전체 비교를 진행하므로 `O(n^2)`이다. 이미 정렬되어 있는 경우 한 번씩 밖에 비교를 하지 않으므로 `O(n)`이다.


```python
def InsertionSort(List): #오름차순
    for size in range(1, len(List)):
        val = List[size]
        i = size
        while i > 0 and List[i-1] > val:
            List[i] = List[i-1]
            i -= 1
        List[i] = val
```

## Bubble Sort(버블 정렬)
버블 정렬은 매번 연속된 두 개의 인덱스를 비교하여, 정한 기준의 값을 뒤로 넘겨 정렬하는 알고리즘이다. 오름차순으로 정렬하고자 하는 경우, 비교할 때마다 큰 값이 뒤로 이동하여, 1바퀴를 돌면 가장 큰 값이 맨 뒤에 저장된다. 맨 마지막에는 비교하는 수들 중 가장 큰 값이 저장되기 때문에, (n - 현재 순환한 바퀴 수)만큼만 반복해주면 된다. 알고리즘은 다음과 같다.

1. 배열의 두번째 인덱스부터 시작하여, 현재 인덱스 값과 바로 이전의 인덱스 값을 비교한다.
2. 이전 인덱스의 값이 더 크면, 현재 인덱스의 값과 바꿔준다.
3. 현재 인덱스의 값이 더 크면, 교환하지 않고 다음 두 연속된 인덱스에 대해 비교한다.
4. 이를 (전체 배열의 크기 - 현재까지 순환한 바퀴 수)만큼 반복한다.

`시간 복잡도`는 배열에서 n-1, n-2, ..., 2, 1개의 원소에 대해 전체 비교를 진행하므로 `O(n^2)`이다. 이미 `정렬된 배열`에서는 `O(n)`이다.

```python
def BubbleSort(List): #오름차순
    for size in reversed(range(len(List))):
        for i in range(size):
            if List[i] > List[i+1]:
                List[i], List[i+1] = List[i+1], List[i]
```

## Heap Sort(힙 정렬)
힙 정렬은 힙(우선순위 정렬된 완전 이진 트리)을 이용하여 정렬하는 알고리즘이다. 힙 정렬을 수행하기 위해서는 주어진 데이터를 가지고 우선 최대 혹은 최소 힙을 구성해야한다. 알고리즘은 다음과 같다.

1. 오름차순의 경우, 주어진 원소들로 최대 힙을 구성한다.
2. 최대 힙의 루트 노드(=현재 배열의 첫번째 원소=최댓값)와 말단노드(=현재 배열의 마지막 원소)를 교환준다.
3. 새로운 루트 노드에 대해 최대 힙을 구성한다.
4. 원소의 개수만큼 2와 3을 반복 수행한다.

`시간 복잡도`는 힙 트리의 전체 높이가 완전 이진 트리이므로 logn이고, 하나의 원소를 삽입하거나 삭제할 때 힙을 재구조화하는데에 logn이 소요된다. 원소의 개수가 n이므로 전체적으로 `O(nlogn)`이다.

```python
def heapify(List, index, heap_size):
    largest = index
    li = 2 * index + 1
    ri = 2 * index + 2
    if li < heap_size and List[li] > List[largest]:
        largest = li
    if ri < heap_size and List[ri] > List[largest]:
        largest = ri
    if largest != index:
        List[largest], List[index] = List[index], List[largest]
        heapify(List, largest, heap_size)

def HeapSort(List): #오름차순
    n = len(List)
    for i in range(n // 2 - 1, -1, -1): #bulid max heap
        heapify(List, i, n)
    for i in range(n - 1, 0, -1):
        List[0], List[i] = List[i], List[0]
        heapify(List, 0, i)
```

## Merge Sort(합병 정렬)
합병 정렬은 분할 정복(Divide and Conquer)방식으로 설계된 정렬 알고리즘이다. 분할 정복은 큰 문제를 작은 문제로 쪼개어 문제를 해결해나가는 방식으로, 분할된 배열의 크기가 1보다 작거나 같을 때까지 반복한다.

입력으로 하나의 배열을 받고, 연산 중에 두 개의 배열(subset)로 계속 쪼개어 나간 후, 모든 subset의 크기가 1보다 작거나 같아지면 다시 합치면서 하나의 정렬을 만든다. 알고리즘은 다음과 같다.

- 분할
1. 현재 배열을 반으로 쪼갠다. 배열의 중간 인덱스를 기준으로 나눈다.
2. 이를 쪼갠 배열의 크기가 0이거나 1일 때까지 반복하여 쪼갠다.
- 정복과 합병
3. 조깨어진 두 배열의 값을 처음부터 하나씩 비교한다. 오름차순의 경우 이 둘 중에 작은 값을 새 배열에 저장한다.
4. 둘 중에 하나가 끝날 때까지 이 과정을 되풀이한다.
5. 만약 둘 중에 하나의 배열이 먼저 끝나게 되면 나머지 배열의 값들을 전부 새 배열에 저장한다.
6. 정렬된 새 배열을 원래의 배열로 옮긴다.

`시간 복잡도`는 분할에서 배열의 크기를 2번씩 쪼개므로 전체를 모두 쪼개면 O(logn), 합병에서 배열의 크기만큼 합쳐주므로 O(n), 각 분할별로 합병을 진행하므로 전체의 시간 복잡도는 `O(nlogn)`이다.

```python
def MergeSort(List): #오름차순
    if len(List) > 1:
        mid = len(List)//2
        lList, rList = List[:mid], List[mid:]
        mergeSort(lList)
        mergeSort(rList)
        li, ri, i = 0, 0, 0
        while li < len(lList) and ri < len(rList):
            if lList[li] < rList[ri]:
                List[i] = lList[li]
                li += 1
            else:
                List[i] = rList[ri]
                ri += 1
            i += 1
        List[i:] = lList[li:] if li != len(lList) else rList[ri:]
```

## Quick Sort(퀵 정렬)
퀵 정렬은 분할 정복(Divide and Conquer)방식으로 설계된 정렬 알고리즘이다. pivot point라는 특정 기준 값을 잡아, 이 값을 기준으로 작은 값은 왼쪽, 큰 값을 오른쪽으로 옮기는 방식의 정렬을 진행한다. 이를 반복하여 분할된 배열의 크기가 1이 되면 배열이 모두 정렬된 것이다. 알고리즘은 다음과 같다.

1. 배열에서 pivot point로 잡을 값을 하나 정한다. 보통 맨 앞이나 맨 뒤, 혹은 전체 배열 값 중 중간값이나 무작위 값으로 정한다.
2. 오름차순의 경우, 배열의 값들을 pivot과 비교하면서 작은 값은 왼쪽 배열, 큰 값은 오른쪽 배열, 같은 값은 중앙 배열에 저장한다.
3. 왼쪽 배열과 오른쪽 배열에 대해서 다시 퀵 정렬을 진행한다.
4. 크기가 1인 배열들을 모두 더해 정렬된 배열을 만든다. 

`시간 복잡도`는 분할에서 pivot point를 기준으로 배열의 크기를 2번씩 쪼개므로 전체를 모두 쪼개면 O(logn), 합병에서 배열의 크기만큼 비교하므로 O(n), 각 분할별로 비교를 진행하므로 전체의 시간 복잡도는 평균적으로 `O(nlogn)`이다. 하지만 `최악의 경우(이미 정렬된 배열)`에 분할이 n번 일어나므로 `O(n^2)`이다.

```python
def QuickSort(List): #오름차순
    if len(List) <= 1:
        return List
    pivot = List[len(List) // 2]
    lesserList, equalList, greaterList = [], [], []
    for num in List:
        if num < pivot:
            lesserList.append(num)
        elif num > pivot:
            greaterList.append(num)
        else:
            equalList.append(num)
    return QuickSort(lesserList) + equalList + QuickSort(greaterList)
```

## Speed Comparison(속도 비교)
|  <center>Name</center> |  <center>Best</center> |  <center>Worst</center> |  <center>Runtime-Avg(정수 60000개) (sec)</center> |
|:--------|:--------:|--------:|--------:|
|**선택 정렬(Selection Sort)** | <center> n<sup>2 </center> |<center> n<sup>2 </center> |<center> 10.842 </center> |
|**삽입 정렬(Insertion Sort)** | <center> n </center> |<center> n<sup>2 </center> |<center> 7.438 </center> |
|**버블 정렬(Bubble Sort)** | <center> n </center> |<center> n<sup>2 </center> |<center> 22.894 </center> |
|**힙 정렬(Heap Sort)** | <center> nlog<sub>2</sub>n </center> |<center> nlog<sub>2</sub>n </center> |<center> 0.034 </center> |
|**합병 정렬(Merge Sort)** | <center> nlog<sub>2</sub>n </center> |<center> nlog<sub>2</sub>n </center> |<center> 0.026 </center> |
|**퀵 정렬(Quick Sort)** | <center> nlog<sub>2</sub>n </center> |<center> n<sup>2 </center> |<center> 0.014 </center> |

일반적으로 버블 정렬 < 선택 정렬 ≒ 삽입 정렬 << 힙 정렬 << 합병 정렬 << 퀵 정렬 순으로 수행 시간이 적게 걸림을 알 수 있다.

퀵 정렬의 최악의 경우 때문에 합병 정렬보다 느린 알고리즘이라고 생각하기 쉽지만, 발생하기 쉽지 않은 경우이고, 일반적으로 퀵 정렬이 합병 정렬보다 20%이상 빠르다.

합병 정렬에서 저장 수단을 배열이 아닌 연결 리스트(linked-list)로 구성한다면, 링크 인덱스만 변경되므로 데이터의 이동은 무시할 정도로 작아진다. 따라서 크기가 큰 배열을 정렬할 경우에 연결 리스트를 이용한다면, 합병 정렬은 퀵 정렬보다 효율적일 수 있다.


### 관련 문제
- https://leetcode.com/problems/k-closest-points-to-origin/
- https://leetcode.com/problems/valid-anagram/


### 참고
- Tim Sort: https://en.wikipedia.org/wiki/Timsort
- Sorting Speed Comparison: https://stackabuse.com/sorting-algorithms-in-python/#sortinginpython
- python code: http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html
- explain: https://hsp1116.tistory.com/33
