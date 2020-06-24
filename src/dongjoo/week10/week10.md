## level 4

##### lyrics

```python
# https://programmers.co.kr/learn/courses/30/lessons/60060

# 3rd try:
def is_match(word, pattern):
    if len(word) != len(pattern):
        return False

    # find question mark index
    idx = 0
    if pattern[0] == '?':
        while pattern[idx] == '?':
            idx += 1
        return pattern[idx:] == word[idx:]
    else:
        idx = pattern.index('?')
        return pattern[:idx] == word[:idx]


def solution(words, queries):
    answer = []
    count = 0
    for query in queries:
        for word in words:
            if is_match(word, query):
                count += 1
        answer.append(count)
        count = 0
    return answer

# 효율성 테스트에서 자꾸 떨어짐 ㅠㅠ
```
##### courses

```python
# https://programmers.co.kr/learn/courses/30/lessons/17685
from collections import defaultdict

class Node:
    def __init__(self, child=None, value=""):
        self.child = child
        self.value = value
    def __repr__(self):
        if self.value == "":
            return 'root node, empty string'
        return self.value


def build_tree(words):
    # alphabet = 'abcdefghijklmnopqrstuvwxyz'
    root = Node()
    build_tree_recursive(words, root)
    return root

def build_tree_recursive(words, parent):
    print(words, parent)
    child_dict = dict()
    if len(words) == 1:
        if not words[0]:
            return 
        child_dict[words[0][0]] = Node(None, words[0])
        parent.child = child_dict
        return parent.child
    
    prefix_dict = defaultdict(list)
    
    for word in words:
        if word != "":
            prefix_dict[word[0]].append(word[1:])
            # child_dict[word[0]] = 
    for prefix in prefix_dict:
        temp_parent = Node(None, prefix)
        temp_parent.child = build_tree_recursive(prefix_dict[prefix], temp_parent)
    return parent.child


root = build_tree(['word', 'war', 'warrior', 'world'])
print(root.child)
print(root)


def solution(words):
    answer = 0
    return answer

# 좀 어려워서 시간 많이 걸림, 진행 중
```
