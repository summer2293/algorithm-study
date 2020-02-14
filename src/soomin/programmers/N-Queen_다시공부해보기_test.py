import pytest
import collections
import re

testdata = [
    (1, 1),
    (2, 0),
    (3, 0),
    (4, 2),
    (5, 10),
    (6, 4),
]

@pytest.mark.parametrize("n, expected", testdata)

def test_simple(n, expected):
    assert solution(n) == expected

def promising(i,col):
    k=0
    correct=True
    while (k<i and correct): 
        if (col[i]==col[k] or abs(col[i]-col[k])==i-k):
            correct=False
            break
        k+=1
    return correct

def queens(n,i,col,count):
    if (promising(i,col)): # queue 배치할 수 있는지 체크 
        if (i==n-1):
            count.append(col)
        else:
            for j in range(n):
                col[i+1]=j
                queens(n,i+1,col,count)

def solution(n):
    col= [0] * n  
    global count
    count=[]
    queens(n,-1,col,count)
    return len(count)

# https://geonlee.tistory.com/40