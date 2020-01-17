# 예산 https://programmers.co.kr/learn/courses/30/lessons/12982
def budget(d, budget):
    """예산(budget)과 부서별 신청한 금액(d)이 주어지면 최대 몇 팀에게 지원할 수 있는지 구한다.

    시간 복잡도:
    d의 길이를 n이라고 할 때 O(nlogn)

    """
    d.sort()
    
    for index, money in enumerate(d):
        budget -= money
        if budget < 0:
            return index
    return len(d)

def test_budget():
    assert budget([1, 3, 2, 5, 4], 9) == 3
    assert budget([2, 2, 3, 3], 10) == 4
