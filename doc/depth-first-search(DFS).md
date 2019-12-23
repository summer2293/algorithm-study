# DFS, Depth First Search(깊이 우선 탐색)

> _by KunhoKim, <https://github.com/kimkunho980422>_



## 개념 
그래프 탐색 기법 중 하나. (그래프 탐색: 하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것)
깊이 우선 탐색은 임의의 노드(vertex)에서 시작해서 다음 분기(branch)로 넘어가기 전에 해당 분기를 완벽하게 탐색하는 방법이다.
탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상 갈 수 없게 되면 다시 가장 가까운 갈림길로 돌아와서 이곳으로부터 다른 방향으로 다시 탐색을 진행한다. 보통 모든 노드를 방문하고자 할 때 사용한다.
`시간 복잡도`는 n개의 정점(vertices)과 m개의 간선(edge)을 가지는 그래프를 DFS할때 `O(n+m)`의 시간이 소요된다. 


## DFS의 진행과정
![DFS의 진행과정](https://gmlwjd9405.github.io/images/algorithm-dfs-vs-bfs/dfs-example.png)

1. 시작 정점(0)을 방문한다. 방문한 노드는 방문했다고 표시한다.
2. 시작 정점(0)과 인접한 정점들을 차례로 순회한다. (0)과 인접한 정점이 없다면 종료한다.
3. (0)과 인접한 정점 (1)을 방문했다면, (0)과 인접한 또 다른 정점을 방문하기 전에 (1)의 이웃 정점를 전부 방문해야한다. (1)을 시작 정점으로 DFS를 다시 시작하여 (1)의 이웃 정점들을 방문한다.
4. (1)의 분기를 전부 완벽하게 탐색했다면, 다시 (0)에 인접한 정점들 중에 아직 방문하지 않은 정점을 찾아 방문한다.
    - 아직 방문하지 않은 정점이 없다면 탐색을 종료한다.
    - 방문하지 않은 정점이 있다면 그 정점을 시작으로 DFS를 시작한다.


## DFS의 구현
### 재귀적 구현
```python
def dfs_visit(graph, start_vertex, visited):
    visited.append(start_vertex)
    for adjacent_vertex in graph[start_vertex]:
        if adjacent_vertex not in visited:
            dfs_visit(graph, adjacent_vertex, visited)

def dfs(graph, start_vertex):
    visited =[]
    dfs_visit(graph, start_vertex, visited)
    return visited


G1 = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6], 6:[], 7:[8], 8:[]}
print (DFS(G1, 1))

# Output: [1, 2, 3, 5, 6, 7, 8, 4]
```

### 스택을 통한 구현
```python
def dfs(graph, start_vertex):
    tovisit = [start_vertex]
    visited = []
    while tovisit:
        current_vertex = tovisit.pop()
        visited.append(current_vertex)
        for adjacent_vertex in graph[current_vertex]:
            if adjacent_vertex not in visited and adjacent_vertex not in tovisit:
                tovisit.append(adjacent_vertex)
    return visited


G1 = {1:[2,3], 2:[3,4,5], 3:[5,7,8], 4:[5], 5:[6], 6:[], 7:[8], 8:[]}
print (dfs(G1,1))

# Output: [1, 3, 8, 7, 5, 6, 2, 4]
```

### 관련 문제
- https://leetcode.com/problems/symmetric-tree/
- https://leetcode.com/problems/course-schedule/


### 참고
- explain: https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html
- image: https://gmlwjd9405.github.io/2018/08/14/algorithm-dfs.html
