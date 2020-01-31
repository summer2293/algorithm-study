import pytest
from collections import deque
import re


@pytest.mark.parametrize("triangle, expected", [
    ([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]], 30)
])


def test_simple(triangle, expected):
    assert solution(triangle) == expected


from collections import deque

def solution(triangle):
    for col in range(1, len(triangle)):
        for row in range(len(triangle[col])):
            
            if row == 0: 
                triangle[col][row] += triangle[col-1][row]
            elif row+1 == len(triangle[col]):
                triangle[col][row] += triangle[col-1][row-1]
            else:
                triangle[col][row] += max(triangle[col-1][row], triangle[col-1][row-1])
    return max(triangle[-1])