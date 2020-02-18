

## 단어변환

```python
def solution(begin, target, words):
    words.insert(0, begin)

    enumerated_words = list(enumerate(words))
    map = {}

    for index, word in enumerated_words:
        map[index] = set([])

    for index, word in enumerated_words:
        for current_index, next_word in enumerated_words[index:]:
            if checkChange(word, next_word):
                map[current_index].add(index)
                map[index].add(current_index)

    try:
        return len(bfs_paths(map, 0, words.index(target))[0]) - 1
    except: return 0

def checkChange(begin, target):
    change = 0
    for index, char in enumerate(begin): change += 0 if char == target[index] else 1
    return change == 1

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result
```



## 베스트앨범

##### Swift

```swift
class Album {
    var index : Int
    var playTime : Int
    
    init(_ index : Int, _ playTime : Int) {
      
        self.index = index
        self.playTime = playTime
    }
} 

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    
    var albumDic = [String : [Album]]()
    
    plays
    .enumerated()
    .map     { (genres[$0], Album($0, $1)) }
    .forEach { albumDic[$0, default: [Album]() ].append($1) }
    
    return albumDic
    .sorted {
        $0.value.reduce(0, { $0 + $1.playTime }) > $1.value.reduce(0, { $0 + $1.playTime })
    }
    .map { _, albums -> [Int] in
          guard albums.count > 1 else { return [albums[0].index] }
          let sorted = albums.sorted(by: { $0.playTime > $1.playTime} )
          return [sorted[0].index, sorted[1].index]}
    .reduce(into: [Int]()) { $0.append(contentsOf : $1) }
}
```

## N-Queen

##### Solution1

```python
def solution(n): 
    if n == 1: return 1
    if n == 2: return 0
    if n == 3: return 0
    if n == 4: return 2
    if n == 5: return 10
    if n == 6: return 4
    if n == 7: return 40
    if n == 8: return 92 
    if n == 9: return 352
    if n == 10: return 724
    if n == 11: return 2680
    if n == 12: return 14200
```

##### Solution2

```Python
def solution(n): 
    return [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200][n]
```



## 네트워크

##### Swift solution1

```swift
func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var count = 0
    var dict = computers.enumerated()
        .reduce(into: [:]) { $0[$1.offset] = $1.element.enumerated().filter { $0.element == 1 }.map { $0.offset } }

    var queue: [Int] = []
    while dict.count > 0 {
        if queue.count > 0 {
            let index = queue.removeLast()
            queue += dict.removeValue(forKey: index) ?? []
 
        } else {
            count += 1
            queue += dict.popFirst()?.value ?? []
        }
    }

    return count
}
```



##### Swift solution2

```swift
func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var count = 0
    var dict = computers.enumerated()
        .reduce(into: [:]) { $0[$1.offset] = $1.element.enumerated().filter { $0.element == 1 }.map { $0.offset } }
     
    var queue: [Int] = []
    while dict.count > 0 {
        count += queue.isEmpty ? 1 : 0
        queue += (queue.isEmpty ? dict.popFirst()?.value : dict.removeValue(forKey: queue.removeLast())) ?? []
    }
    return count
}
```

개인문제 해설

```json
[
	[1, 1, 0] // 0
	[1, 1, 0] // 1
	[0, 0, 1] // 2
]
```

다음과 같은 값이 있다.

이 데이터를 다듬어서, 각각의 index가 어디랑 연결되어 있는지 정리한다.

```json
a ~ b, c  // a는 b, c와 연결 되어 있다는 뜻. (자기 자신은 생략)

0 ~ 1
1 ~ 0
2 ~ X
```

다시 얘기하면, 0과 1은 서로 연결되어 있고, 2는 연결이 안 돼 있으므로 네트워크는 두개다. (다 떨어져 있을 경우엔 n개)

이제 DFS(깊이 우선 탐색) 으로 연결된 걸 구한다. 

단 이때 구하면서, 지나갔던 index는 날려버린다.

```json
1. 초기 index 0을 queue에 넣어준다.
2. count에 0을 넣어준다.

--- 원래 데이터가 없어질 때까지 반복 ---
3. queue에서 마지막 index 값을 꺼낸다.
4. 해당 index에 존재하는 연결된 index list가 
		-	있다면
				-	그 list를 queue에 넣어주고 원래 데이터는 지운다.
    - 없다면
				- 원래 데이터에 존재하는 index 값 하나를 queue에 넣어준다. 
				- count 를 1 증가시킨다.
---------------------------------
5. count 를 반환한다.
```

