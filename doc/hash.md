# hash Table

> by Han soomin, <https://github.com/soomtopia>

### 개념

키(key)에 결과 값(value)을 저장하는 데이터 방식. python 에서는 내장 `dictionary` 방식이 있다.  

![img](https://t1.daumcdn.net/cfile/tistory/236B1A4C56B4DE1F12)

### 작동방식

1. __key__ 는 __hash function__ 을 통해 _hash_ 값을 리턴한다
2. 리턴받은 hash 는 bucket 의 index 로 환산되여 데이터에 접근한다. 



### 구성요소

- ##### key 

  고유한값. hash function 의 input 이 된다. key 는 여러 값이 될 수 있기 때문에, 바로 최종 저장소에 저장이 되면 그만큼 공간을 구성해야하기 때문에 비효율적이다. 

- ##### hash function 

  input key  output hash. key 값을 일정한 길이를 가지는 해시로 변경하여 저장소를 효율적으로 운영한다. 

- ##### Hash

  bucket / slot 에 데이터를 색인할 index 

- ##### value

  bucket / slot 에 최종적으로 저장되는 값. 저장 / 삭제 / 검색 / 접근이 가능해야 한다. 

- ##### Bucket / Slot 

  value 가 저장되는 저장소





### 성능

| FUNCTION | BEST | WORST (collision) |
| :------: | :--: | :---------------: |
|  insert  | O(1) |       O(N)        |
|  delete  | O(1) |       O(N)        |
|  search  | O(1) |       O(N)        |



### hash collision

서로 다른 key 가 hash function 을 통해 같은 해시가 될 수 있는 경우를 말한다. 해시 함수 알고리즘을 잘 짜서 줄여야 한다. 

### 해결방법

#### 1. chaining

충돌 시에 해당 index value 값에 연결시키는 방법. 

![chaining](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2015/07/hashChaining1.png)

##### 장점

한정된 저장소를 효율적으로 사용할 수 있다.

적은 메모리 사용하지만, 

##### 단점

검색 효율이 낮아질 수 있다.

외부 저장 공간 작업을 추가로 해야한다 .



#### chaining 시간복잡도

 len(Bucket) ==  ‘N’,  len(key) ==  ‘m’ 일 때, 평균적으로 저장소에서 1개의 hash당 (m/n)개의 키가 들어있다. 이를 ‘α’라고 정의한다.

insert 시 __head__ 에 저장할 경우에는 O(1)의 시간 복잡도를 가지지만 , tail 에 자료를 저장할경우 O(α) 의 시간을 가진다 

```
m/n = α (1개의 Hash당 평균적으로 α개의 키가 들어있다.)
```

|    FUNCTION     | BEST | WORST (collision) |
| :-------------: | :--: | :---------------: |
|     insert      | O(1) |       O(N)        |
| delete & search | O(α) |       O(N)        |



#### 2. open addressing 

![img](https://media.geeksforgeeks.org/wp-content/uploads/Linear-Probing-1-1.jpg)

비어있는 해시를 찾아 데이터를 저장하는 기법. 파이썬 내장함수는 이걸 사용하는듭..?

- 선형탐색 +1 또는 +n 을 통해 비어있는 해시에 데이터를 탐색
- 제곱 탐색: 충돌이 일어난 해시의 제곱을 한 해시에 데이터 저장
- 이중 해시 : 다른 해시 함수를 한번 더 적용한 해시에 데이터저장

##### 장점 

- 해시 테이블 내의 데이터 저장 / 처리 사용
- 저장 공간 추가작업 x

##### 단점

- 함수의 성능이 해시 테이블 성능에 좌지우지된다.
- 데이터 길이가 늘어나면 그에 해당하는 저장소를 마련해야한다.



#### Open Addressing 시간복잡도

len(Bucket) ==  ’n’, len(key) == ‘m’일 때, ‘α’는 1보다 작거나 같다. 

저장소 1개 버킷 당 1개의 값(value)만 가지기 때문이다.

```
m/n = α (α <= 1)
```

|           FUNCTION            | BEST | WORST (collision) |
| :---------------------------: | :--: | :---------------: |
| Insertion & Deletion & Search | O(1) |       O(N)        |