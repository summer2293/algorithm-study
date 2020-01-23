## python 에서는 어떤 알고리즘으로 sorting 을 할까?

정렬 알고리즘을 공부하다보면 , 다양한 알고리즘을 접할 수 있습니다. 

python 에서는 어떤 정렬알고리즘을 통해 sorting 을 할까요?

## Tim sort

python 내부에서는 __tim sort__ 라는 알고리즘을 사용합니다. python 2.3 + 부터, java sdk에서도 사용된다고 하네요.

Tim sort 알고리즘은 insert 정렬과  merge 정렬을 합친 하이브리드 알고리즘으로, _"현실 세계의 데이터는 대략적으로 정렬이 되어있다"_ 는 가정을 가지고 만들어진 알고리즘입니다.

#### 시간복잡도

merge sort 의 최악의 시간 복잡도 _(O(nlogn)_ 와, insert sort 의 최고 시간 복잡도 _(O(N))_ 를 가지게 됩니다.

o(N) ~ o(nlogn)사이를 보장하게 됩니다.

##### 

#### 동작 방식 

일단, 처음부터 요소를 돌며 정렬된 데이터를 체크한다. 

##### run

처음부터 요소를 돌면서, 정렬된 데이터를 체크한다 (오름, 내린). 이 값을 찾고 run 이라 명칭한다.

##### minrun

요소를 돌면서 정렬되지 않는 데이터를을 minrun 이라고 한다. 해당 값은 32개 또는 64개의 값으로 잘라 분류하고,

insert sort를 써서 값을 정렬한다.

> 32 / 64개인 이유 (java는 경험 상 32개가 좋다고 32로 분류한다 함)
>
> - 2의 지수승이 merge sort 로 정렬하기가 쉽고
>
> - 삽입 정렬의 경우 데이터가 작을수록 최대 성능을 낸다고함
>
>   ```
>   그밖에도 배열이 작을 경우에 역시 상당히 효율적이다. 일반적으로 빠르다고 알려진 알고리즘들도 배열이 작을 경우에는 대부분 삽입 정렬에 밀린다. 따라서 고성능 알고리즘들 중에서는 배열의 사이즈가 클때는 O(n\log n)O(nlogn) 알고리즘을 쓰다가 정렬해야 할 부분이 작을때 는 삽입 정렬로 전환하는 것들도 있다.
>   ```
>

#### merge

이렇게 run 을 만들어서 stack 에 보관하는데, 중간중간 merge sort 를 통해 정렬을 한다.

##### merge 조건

1. X > Y + Z
2. Y > Z

stack 아래쪽에 쌓여 있는 run의 len 값이 길이 보다, stack 위쪽에 쌓여 있는 run의 길이가 더 길게 유지되어야한다.

<http://blog.naver.com/PostView.nhn?blogId=talag&logNo=221020181491>



![image](http://postfiles7.naver.net/MjAxNzA2MDJfMTQ0/MDAxNDk2Mzg1NzE2ODM1.p_QNvjjbvIH6W0Wq8VGLWTS82hg9p7Rzi1-FeaG-nncg.NRl3RwYrcs1dTJqIbEEhi-Skl4Tdu3rqm0Dwcc_8ktMg.PNG.talag/2.png)

####  **Galloping mode** 

x,y 비교 시 연속적으로 y에 있는 값보다 적을경우 __chunck__ 를 사용해 한번에 swap 한다.