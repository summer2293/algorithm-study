from collections import deque
def is_reachable(origin, target):
    difference = 0
    for idx in len(origin):
        if origin[idx] != target[idx]:
            difference += 1
        if difference > 1:
            return False
    return True


def solution(begin, target, words):
    explored = set() # all reachale words
    level = [] # words reachable in a level
    tree = deque()
    answer = 0
    changed = True # if size of explored as changed or not
    while changed:
        
        pass




    return answer
