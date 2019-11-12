# Greedy

<img width="300" alt="greedy_word" src="https://user-images.githubusercontent.com/39859458/68653602-6dcece80-056f-11ea-9191-33af37afa8b5.png”>

## 개념
**매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 적합한 결과를 도출하자.**
그리디 알고리즘은 탐욕 알고리즘 또는 욕심쟁이 알고리즘이라고 한다. 미래를 생각하지 않고 각 단계에서 가장 최선의 선택을 하는 기법이다. 이렇게 각 단계에서 최선의 선택을 한 것이 전체적으로도 최선이길 바라는 알고리즘이다.

1. (입력) 데이터 간의 관계를 고려하지 않고 수행 과정에서 '욕심내어' 최소값 또는 최대값을 가진 데이터를 선택한다.
2. 이러한 선택을 '근시안적'인 선택이라고도 한다.
3. 그리디 알고리즘은 근시안적인 선택으로 부분적인 최적해(locally optimal solution)를 찾고, 이들을 모아서 문제의 최적해(globally optimal solution)를 얻는다. 
3-1. 부분적은 집합(멱집합, power set)이라는 수학적 개념을 이용하여 문제를 풀고, 현실세계의 비선형 문제중 하나 인 최단 경로 구하기(Graph)의 근사해로 많이 이용된다. 
3-2. 여러가지 상황들을 고려 (비선형적인 trade-off, graph)

*Keyward: 최적화문제풀이용 알고리즘, 근시안적, 근사치 ,욕심 

## 예시
1. 수업 시간표 짜기 문제. 
- 당신은 학교에서 되도록 많은 수업을 듣고 싶어한다. 당신이 신청할 수 있는 과목의 목록은 다음과 같다. 
    <img width="300" alt="greedy_word" src="https://user-images.githubusercontent.com/39859458/68653790-d3bb5600-056f-11ea-8a12-188673a80276.jpg”>



    1) 가장 빨리 끝나는 과목을 고란다. 
    2) 첫번째 과목이 끝난 후에 시작하는 과목을 고른다. 

- 각 단계에서 국소 최적해(locally optimal solution)을 찾음으로써 최종적으로는 전역 최적해(globally optimal solution)을 구현한다. 


(항상 최적의 해를 찾을까?)
2. 배낭 채우기 문제. 
- 도둑이 훔친 물건을 가져갈 배낭을 갖고 있다. 이 배낭에는 총 35kg의 물건만 넣을 수 있다. 
- 훔친 물건 list는 아래와 같다. 
    <img width="300" alt="P1_1" src="https://user-images.githubusercontent.com/39859458/68653852-f77e9c00-056f-11ea-84f6-8ab9c0d7a961.png">


    1) greedy알고리즘으로 이 문제를 풀면 : 스테레오(30kg), 총가치 3000달러. 
    2) 그러나, 노트북(20kg), 기타(15kg)를 넣으면 총치 3500달러이다. 
- 그리드 알고리즘은 올바른 답을 내놓지 못했다. 그러나 정답에 상당히 가까운 답을 낸다. 

즉, 이 그리디 알고리즘은 너무 깊이 고민하지 않고(=과부하 없이) 최적(=최선)의 해를 구하는 경우에 사용하면 좋은 알고리즘이다. 

- 동적 프로그래밍에 적합한 알고리즘!!! 

3. 최단 경로 구하기 // 최소 망 개수 구하기. 
- 미국 50개 주의 모든 사람에게 라디오 쇼를 들려주려고 할때, 
- 가장 적은 수의 방송국 수를 구해보는 문제. 

    1) 가능한 모든 방송국의 부분 집합을 나열합니다. 
    - 멱집합 
    (https://ict-nroo.tistory.com/51)
    (https://ko.wikipedia.org/wiki/%EB%A9%B1%EC%A7%91%ED%95%A9)
    (https://ko.wikipedia.org/wiki/%EC%B9%B8%ED%86%A0%EC%96%B4%EC%9D%98_%EC%A0%95%EB%A6%AC)
    2) 가능한 부분 집합의 수는 2^n이다. 
    3) 이 부분 집합 중에서 50개 주 전체를 커버할 수 있으면서 가장 원소의 수가 적은 부분 집합을 고른다.  

- 실제 코드는 문제 단순화를 위해 8개의 주만
    <img width="300" alt="P1_1" src="https://user-images.githubusercontent.com/39859458/68653748-bc7c6880-056f-11ea-9843-00d4ff18b2a3.jpg">


```python
#방송하고자 하는 주의 목록을 넣는다. 
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#선택된 방송국의 목록이 필요하므로 이 목록을 저장하는 해시 테이블(dict)을 만든다. 
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#방문할 방송국의 목록
final_stations = set()

#아직 방송이 되지 않은 주 중에서 가장 많은 주를 커버하고 있는 방송국을 고르는 코드. 
#방문할 방송국의 목록 = best_station: greedy기법(=사고법)으로 가장 cover하는 지역이 많은 방송국을 우선 고른다.
#best_station변수에 넣는다. (final_station.add(best_station))
#states_needed를 갱신한다. (-=)
#for문으로 반복

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
        
        states_needed -= states_covered
        final_stations.add(best_station)

print(final_stations)
>>> 'ktwo', 'kthree', 'kone', 'kfive'

```

## 관련 개념. 
1. 집합: 멱집합
2. graph
3. NP완전문제(Nondeterministic Polynomial-. Complete), 집합 커버링 문제(set-covering problem)
    - NP 집합에 속하는 결정 문제 중에서 가장 어려운 문제의 부분집합으로, 모든 NP 문제를 다항 시간 내에 NP-완전 문제로 환산할 수 있다. NP-완전 문제 중 하나라도 P에 속한다는 것을 증명한다면 모든 NP 문제가 P에 속하기 때문에, P-NP 문제가 P=NP의 형태로 풀리게 된다. 반대로 NP-완전 문제 중의 하나가 P에 속하지 않는다는 것이 증명된다면 P=NP에 대한 반례가 되어 P-NP 문제는 P≠NP의 형태로 풀리게 된다.

#### 그래프
<img width="500" alt="G1" src="https://user-images.githubusercontent.com/39859458/68653936-2dbc1b80-0570-11ea-86d1-d7f0add5e70d.png">

<img width="500" alt="G2" src="https://user-images.githubusercontent.com/39859458/68653966-3f052800-0570-11ea-9ba7-8214270c12db.png">



#### NP문제 예시: 가장 훌륭한 풋볼 팀 선수 고르기. 
   <img width="300" alt="football" src="https://user-images.githubusercontent.com/39859458/68654366-1cbfda00-0571-11ea-8677-e1e29d3a2bb4.png">

- https://ko.wikipedia.org/wiki/NP-%EC%99%84%EC%A0%84



# 관련 문제

[leetcode-921.Minimum Add to Make Parentheses Vlalid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)

[leetcode-861.Score After Flipping Matrix](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

# 출처

- [알고리즘, 사이텍미디어 출판 - 오경수/강희중/안효범/임재걸 공역]
- [Hello Coding 그림으로 개념을 이해하는 알고리즘]
