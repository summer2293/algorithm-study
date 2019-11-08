## python-algorithm-tmi

python 공부하면서 알게되는 잡다한 파이썬 지식 모음



## TMI 

#### 1. 삼항 연산자 파이썬 사용법 

```ruby
result = condition ? when True : when False;
```

원래 보통 이런식으로 c, java 는 작성하나 파이썬은 달랐다

```python
result = (a-b) if a == b else (a+b)    # 결과는 a+b = 30
```



#### 2. / vs // 

파이썬은 나눌때 실수로 반환된다!!! 자바와 같은 정수형 반환이 되지않아 당황했음. 

정수형 반환을 원하면 _//_ 를 사용하면 된다 

```python
>>> 4/2
2.0
>>> 4//2
2
```



#### 3. is 연산자

> http://seorenn.blogspot.com/2011/04/python-is.html

'is' 연산자는 포인터(레퍼런스)를 비교하는 연산자. 데이터를 비교하는 연산자가 아니다. 'is' 커맨드는 가급적이면 상수(None, True, False 등)를 비교하는데만 쓰도록 하자. 예를 들자면 varA is not None 이런 식으로...



#### 4. try - except vs if else

> <https://moltak.tistory.com/4>

##### if / else 와 try-except 중 뭘 써야할지 굉장히 많이 토론이 되는 토픽이라고 한다. 

- 효율적 측면
  - 99% try문을 통과할시 try, except 를 쓰는게 낫고 50%이상이 try문을 통과하지 못할시 if else를 쓰는게 효율적
- 그 외 참고할 자료:  `None` 보다 예외를 발생시키자 (Effective Python: Better way 14)
  - `None`을 반환하는 함수는 후에 호출할 때 해당 값이 `None`인지 평가해줘야함 ( `if return_none_or_value() == None else…`)
  - 코드를 읽는 사람이 왜 `None`을 반환하는지 명확하게 유추할 수 없음 -> `raise CustomException`을 발생시켜서 명확히 어떤 상황인지 명시하는게 



#### 5. ^ - XOR 비트 상호배제 

> 비트 상호배제는 같은 자리의 값이 서로 다르면 해당 자리의 연산 결과가 1이며 같을 때 0입니다. 예를 들어 a가 6이고 b가 3일 때 a^b는 5입니다.(110^011 => 101) 

```python
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for elem in nums:
            answer = answer ^ elem
```



#### 6. for _ in range(k)

인덱스를 쓸 일이 없을 경우 이런식으로 쓸 수 있다.



#### 7. sort 와 sorted의 차이

- __sort()__
  원본을 직접 정렬 , None을 반환함

  ```python
  list.sort()
  ```

- __sorted(list)__
  리스트가 아닌 값을 솔팅함. 원본에 영향을 끼치지 않음, 정렬한 새로운 __문자열__ 혹은 list를 반환함



#### 8. collections.Counter()

문자열 갯수 새는 로직을 짤때, 하나하나 hash 로 안해줘도됨. Counter 가 알아서 해준다! 

- most_common(n)
  입력된 값의 요소들 중 빈도수(frequency)가 높은 순으로 상위 n개를 리스트(list) 안의 투플(tuple) 형태로 반환한다. n을 입력하지 않은 경우, 요소 전체를 [(‘값’, 개수)]의 형태로 반환한다.

  ```python
  import collections
  
  c2 = collections.Counter(‘apple, orange, grape’)
  print(c2.most_common())
  print(c2.most_common(3))
  ```

  > =  `heapq.nlargest(k, counter.keys(), key=counter.get) `

##### 

#### 9. bisect

정렬된 리스트를 삽입 후에 다시 정렬할 필요 없도록 관리할 수 있도록 지원. 본 기능 이외에 구간의 인덱스를 얻을 때도 유용하게 사용할 수 있다.

##### bisect.bisect(a, x, lo=0, hi=len(a))

```python
>>> arr = [1,4,6,9,11]
>>> bisect.bisect(arr,3)
1
>>> bisect.bisect_right(arr,3)
1
```

__bisect.bisect_left()__  또는 __bisect.bisect_right()__ 가 존재하는데, default 는right.

정렬하는 배열 값의 인덱스에 같은 값이 있을 경우, 왼쪽에 정렬할지, 오른쪽에 정렬할지에 대한 내용을 알려준다. 



#### 10. hash value 로 sorting 하고 싶을 경우 

```python
import operator
x = {'1': 2, '3': 4, '4': 3, '2': 1, '0': 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
```



## interview

#### 자료를 소팅된 상태로 저장해야 한다면 무슨 자료 구조를 써야 할까요? 

(p.s 면접 담당자가 좋아함)

> 트리를 사용할 것 같다. in order traversal 방식을 사용하면 자동으로 소팅이 되어있다. 
>
> or
>
> AVL 트리는 모든 internal node v에 대해, v의 자식들의 높이가 최대 1만큼만 차이가 나는 이진 탐색 트리이다. insert나 remove할 때 높이차가 2이상이면, 데이터를 재구조화하기 때문에 유용할 것 같다! 



