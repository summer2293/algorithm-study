# Graph

## 정의
정점(버텍스)과 간선(아크)들로 이루어진 집합. 즉 트리 역시 그래프에 속한다 할 수 있다.

## 그래프 종류

![방향그래프](https://cdn.filepicker.io/api/file/ASqFe9MSQXqzoZthyThq)

방향그래프 VS 무방향 그래프
```
방향그래프(Directed Graph): 간선에 방향이 존재하는 그래프
A->B로만 갈수있는 간선은 <A,B>로 표현
<A,B> != <B,A>
ex) 일방통행
```
```
무방향그래프 (Undirected Graph):무방향 그래프의 간선은 간선을 통해서 양방향으로갈 수있다.
정점 A와 정점 B를 연결하는 간선은 (A,B)와 같이 정점의 쌍으로 표현한다.
(A,B) = (B,A)
ex) 양방향통행도로
```

## 그래프의 구현

### 인접행렬(Adjacent Matrix)
```
정점이 N개라면 N*N행렬을 만들어서 각각에 연결된 간선들을 표시
두 정점이 인접되어 있으면 정점을 나타내는 행과 열에 대한 행렬값을 1, 인접되어있지 않으면 행렬값 0
```
![인접행렬-방향그래프](https://t1.daumcdn.net/cfile/tistory/21029250584C0F2413)

### 인접행렬 - 방향그래프
![인접행렬-무방향그래프](https://t1.daumcdn.net/cfile/tistory/2405384D584C11BC2E)

### 인접행렬 - 무방향그래프 

### 인접리스트(Adjacent List)
``` 
각 정점에 인접한 정점들을 단순 연결 리스트로 만드는 것
순서상관없음
```
![인접리스트-방향그래프](https://t1.daumcdn.net/cfile/tistory/2269874B584C17F301)

![인접리스트-무방향그래프](https://t1.daumcdn.net/cfile/tistory/265E074D584C26DD2B)

```
간단한 구조의 그래프는 인접행렬로 구현이 가능하나 시간복잡도 O(n^2)이 걸리기 때문에 그래프의 정점이 많은 경우O(n)이 걸리는 인접리스트로 구현하는 것이 효율적
```

## 다익스트라(Dijkstra) 최단 경로 알고리즘

```
그래프에서 정점끼리의 최단 경로를 구하는 법 
하나의 정점으로부토 모든 다른 정점까지의 최단 경로를 찾는 알고리즘
무방향,방향그래프에 모두 적용 가능

```

### 원리
```
시작 정점 v에서 가장 가까운 정점을 선택하여 추가하면서 추가된 새로운 정점에 의해 단축되는 경로가 있으면, 경로 거리를 수정하는 과정을 반복하면서 시작정점에서 모든 정점에 대한 최단 경로를 구하는 것 
distance[w] <- min(distance[w], distance[u]+distance[u][w])
```
- 데이터의 의미
- S = 방문한 노드들의 집합
- d[N] = A -> N까지 계산된 최단 거리
- Q = 방문하지 않은 노드들의 집합

1. 다익스트라 알고리즘은 아직 확인되지 않은 거리는 전부 초기값을 무한으로 잡는다.

2. 루프를 돌려 이웃 노드를 방문하고 거리를 계산한다.

3. 첫 루프 이후의 그래프 상태가 업데이트되는 방식


4. 더 빠른경로를 발견한 경우

5. 또 다른 방복 루프 상황

```python
class Graph(object):
    """
    A simple undirected, weighted graph
    """

    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)

    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    current_node = initial_node
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        cur_wt = visited[min_node]

        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node

    return visited, path


def shortest_path(graph, initial_node, goal_node):
    distances, paths = dijkstra(graph, initial_node)
    route = [goal_node]

    while goal_node != initial_node:
        route.append(paths[goal_node])
        goal_node = paths[goal_node]

    route.reverse()
    return route


if __name__ == '__main__':
    g = Graph()
    g.nodes = set(range(1, 7))
    g.add_edge(1, 2, 7)
    g.add_edge(1, 3, 9)
    g.add_edge(1, 6, 14)
    g.add_edge(2, 3, 10)
    g.add_edge(2, 4, 15)
    g.add_edge(3, 4, 11)
    g.add_edge(3, 6, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(5, 6, 9)
    assert shortest_path(g, 1, 5) == [1, 3, 6, 5]
    assert shortest_path(g, 5, 1) == [5, 6, 3, 1]
    assert shortest_path(g, 2, 5) == [2, 3, 6, 5]
    assert shortest_path(g, 1, 4) == [1, 3, 4]

```


