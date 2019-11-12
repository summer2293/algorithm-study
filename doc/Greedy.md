# Tree

## 개념
트리(Tree)는 자료들이 리스트, 스택, 큐와 같은 1:1관계의 선형 구조가 아니라 1:n 관계의 비선형
자료구조입니다. 또한 계층 관계로 만들어진 계층형 자료구조(Hierarchical Data Structure) 입니다.

노드로 이루어진 자료구조

1. 트리는 하나의 루트 노드를 갖는다.
2. 루트 노트는 0개 이상의 자식 노드를 갖고있다.
3. 그 자식 노드 또한 0개 이상의 자식 노드를 갖고있고, 
이는 반복적으로 정의 된다.

- 노드(node)들과 노드들을 연결하는 간선(edge)들로 구성되어 있다.
    - 트리에는 사이클(cycle)이 존재할 수 없다.
    - 노드들은 특정 순서로 나열될 수도 있고, 그럴 수 없을 수도 있다.
    - 각 노드는 부모노드로의 연결이 있을 수도 있고 없을 수도 있다.
    - 각 노드는 어떤 자료형으로도 표현 가능하다.

![tree-terms](https://gmlwjd9405.github.io/images/data-structure-tree/tree-terms.png)


## 용어
- 루트노드(root node):부모가 없는 노드, 트리는 하나의 루트 노드만을 가진다.
- 단말노드(leaf node):자식이 없는 노드, '말단 노드'또는 '잎 노드'라고도 부른다.
- 내부(internal)노드: 단말노드가 아닌 노드
- 간선(edge):노드를 연결하는 선(link, branch라고도 부름)
- 형제(sibling):같은 부모를가지는 노드
- 노드의 크기(size): 자신을 포함한 모든 자손 노드의 개수
- 노드의 깊이(depth): 루트에서 어떤 노드에 도달하기 위해 거쳐야 하는 간선의 수
- 노드의 레벨(level): 트리의 특정 깊이를 가지는 노드의 집합
- 노드의 차수(degree): 하위 트리개수/ 간선 수(degree) = 각 노드가 지닌 가지의 수
- 트리의 차수(degree of degree): 트리의 최대 차수
- 트리의 높이(height): 루트 노드에서 가장 깊숙히 있는 노드의 깊이

## 트리(Tree)의 특징
- 그래프의 한 종류로서, '최소 연결 트리'라고 부름
- DAG(Directed Acyclic Graphs, 방향성이 있는 비순환 그래프)의 한 종류
    - loop나 circuit이 없다. self-loop도 없다.
    - 즉, 사이클이 없다.
- 노드가 N개인 트리는 항상 N-1개의 간선(edge)을 가진다.
    - 간선은 항상(정점의 개수 - 1)만큼을 가진다.
- 루트에서 어떤 노드로 가는 경로는 유일하다.
    - 임의의 두 노드 간의 경로도 유일. 즉, 두 개의 정점 사이에 반드시 1개의 경로만을 가진다.
    

## 이진트리(Binary Tree)
트리의 구조를 일정하게 제한하여 정의하면 트리의 연산이 단순하고 명확해진다. 트리의 모든 노드의 차수를 2이하로 제한하여 전체 트리의 차수가 2이하가 되도록 정의한 것이
이진트리(Binary Tree)입니다.

![트리순회](C:\Users\user\Desktop\알고리즘\트리순회.jpg)


## 이진트리의 순회(Traversal)
순회란 모든 원소를 빠트리거나 중복하지 않고 처리하는 연산을 의미합니다. 리스트, 스택, 큐 등과 같은 자료구조는 원소를 1:1관계를 구성하기 때문에 순회 연산을 별도로 작성할 필요가 없다.
하지만 이진트리는 1:2의 비선형 계층 구조이므로 현재노드를 처리한 후에 어떤 노드를 처리할지 결정하는 기준을 정해 놓은 순회 연산이 필요합니다.

하나의 노드에서 순회를 위해 수행할 수 있는 작업은 세가지로 정의할 수 있다.
```
작업 D: 현재 노드를 방문하여 처리한ㄷ.
작업 L: 현재 노드의 왼쪽 서브 트리로 이동한다.
작업 R: 현재 노드의 오른쪽 서브 트리로 이동한다.
```

노드 정의
```python
class root:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

```

> 전위 순회(pre-order traversal): D -> L -> R

```python
class BinarySerachTree(object):
    ...
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
        if root is None:
            pass
        else:
            print(root.data)
            _pre_order_traversal(root.left)
            _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)
```

> 중위순회(in-order traveral): L -> D -> R

```python
class BinarySearchTree(object):
    ...
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
            _in_order_traversal(root.left)
            print(root.data)
            _in_order_traversal(root.right)
        _in_order_traversal(self.root)
```

>후위 순회(post-order traversal): L -> R -> D

```python
class BinarySearchTree(object):
    ...
    def post_order_traversal(self):
        def _post_order_traversal(root):
        if root is None:
            pass
        else:
            _post_order_traversal(root.left)
            _post_order_traversal(root.right)
            print(root.data)
        _post_order_traversal(self.root)
```

## 이진 탐색 트리(BinarySearchTree)

트리를 효율적으로 구현하고 사용하기 위해서 일정한 조건으로 정의한 것이다. 탐색용 자료구조로 사용되어 노드의 크기에 따라서 위치를 정의한다.
이진 탐색 트리의 경우에는 다음과 같은 규칙을 가지고 있다.

- 모든 원소는 서로 다른 키를 갖는다.
- 왼쪽 서브 트리에는 있는 원소들은 루트의 키보다 작다.
- 오른쪽 서브 트리에 있는 원소들은 루트의 키보다 크다.
- 왼쪽 서브 트리와 오른쪽 서브 트리도 이진 탐색 트리 이다.

1. 클래스 정의 및 초기화
이진트리 구현하려면, 먼저 Node 쿨래스를 정의해야합니다. Node클래스는 노드값인 self.data와 왼쪽/오른쪽 노드인 self.left, self.right 총 세개의 속성을 가집니다. 초기화 할때는 데이터 값만 주어지고 좌우노드는 비어있습니다.

```python
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

```

이제 Node 클래스를 사용해 이진 탐색 트리 클래스인 BinarySearchTree를 구현
처음에는 비어있는 트리 초기화

```python
class BinarySerachTree(object):
    def __init__(self):
        self.root = None
```

2. 삽입/Insert Method

BinarySearchTree에 insert() Method를 구현하여 트리에 새 원소를 추가 할 수 있도록 합니다.
재귀를 이용한 구현! 새로 추가할 원소의 값을 현재 노드의 값과 비교하여 왼쪽/오른쪽 중 알맞은 위치로 노드를 옮겨가면서 삽입위치를 확인.

```python
class BinarySerachTree(object):
    ...
    def insert(self,data):
        self.root = self._insert_value(self.root,data)
        return self.root is not None
    
    def _insert_value(self,node,data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left,data)
            else:
                node.right = self._insert_value(node.right,data)
            return node
```

3. 탐색/Find Method

원하는 값의 존재유무를 확인할 수 있도록, find() Method를 구현
재귀와 값의 대소관계를 비교를 통해 구현가능

```python
class BinarySerachTree(object):
    ...
    def find(self,key):
        return self._find_value(self.root,key)
    
    def _find_value(self,root,key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)
```

4. 삭제/Delete Method

자식이 하나인 경우엔 자식 노드를 삭제한 노드 위치로 가져오면 됩니다.

1. no Child
2. one Child
3. two Child

하지만, 삭제할 노드의 자식이 두개인 경우에는 왼쪽 서브트리와 오른쪽 서브트리를 각각 A,B라고 했을때, B에서 가장 왼쪽 아래에 위치한 자손을 가져옵니다. 이 원소는 A의 모든 원소들 보다는 크면서 , B의 나머지 원소보다 작기때문에 해당 노드를 가져오는 것입니다.

```python
class BinarySearchTree(object):
    ...
    def delete(self,key):
        self.root,deleted = self._delete_value(self.root,key)
        return deleted

    def _delete_value(self,node,key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
            #replace the node to the leftmost of node.right
                parent,child = node,node.right
                while child.left is not None:
                    parent,child = child,child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted =  self._delete_value(node.left,key)
        else:
            node.right,deleted = self._delete_value(node.right,key)
        return node,deleted
```
이진트리의 경우 좌우 균형이 맞는다면 탐색, 삽입, 삭제의 시간복잡도가 O(logn)입니다. 그러나 이진탐색트리는 정렬된 데이터에 취약합니다. 오름차순이든 내림차순이든 정렬된 데이터가 입력되면 한쪽으로 치우진트리가 만들어집니다. 이때, 최악의 경우 모든 데이터를 살펴야 할 수도 있어서 시간복잡도가 O(n)이 됩니다.




# 관련 문제

[leetcode-617.Merge Two Binary Tree](https://leetcode.com/problems/merge-two-binary-trees/)

[leetcode-104.Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

# 출처

[파이썬으로 구현한 자료구조-트리](https://baejino.com/programing/python/datastructure-4-tree)

[python을 이용한 이진 트리와 순회 알고리즘 구현](http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-2.html)

[python을 이용한 이진 탐색 트리 구현](https://geonlee.tistory.com/72?category=318965)
