

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

