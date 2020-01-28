# programmers lv2 스킬트리
# https://programmers.co.kr/learn/courses/30/lessons/49993

import pytest
import collections
import re

def solution(skill, skill_trees):
    count = 0
    for token in skill_trees:
        if check_right_skill_tree(token, skill): count += 1
    return count

def check_right_skill_tree(token, skill):
    stack = []
    for char in token:
       if char in skill:
           if skill.index(char) != len(stack):
               return False
           else:
               stack.append(char)
    return True

if __name__ == "__main__":
    solution(skill, skill_trees)
    