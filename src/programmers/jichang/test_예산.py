# 예산 https://programmers.co.kr/learn/courses/30/lessons/12982
def budget(d, budget):
    d.sort()
    counter = 0
    total = 0
    for money in d:
        total += money
        if total > budget:
            break
        counter += 1
    return counter

def test_budget():
    assert budget([1, 3, 2, 5, 4], 9) == 3
    assert budget([2, 2, 3, 3,], 10) == 4
