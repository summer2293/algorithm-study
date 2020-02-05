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


count = [
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
    solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
]

print(count)
