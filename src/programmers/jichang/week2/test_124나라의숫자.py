"""
숫자를 가만보니 124나라의 숫자는 마지막 자리수가 124로 반복되는 것을 알 수 있었다.
앞자리수도 같은것이 3개씩 있는 묶음으로 반복되는 것을 알 수 있었다.

이를 풀어쓴다면, 
어떤수를 3으로 나눴을 때 나머지가 0, 1, 2이면 124나라로 변환했을 때 각각 4, 1, 2이다.

그리고 어떤수 - 1을 3으로 나눴을 때 몫이 앞의 자리수에 채워진다.
"""


def make_124_number(n):
    if n <= 3:
        return '124'[n-1]
    else:
        return make_124_number((n - 1) // 3) + make_124_number(n % 3)


def test_make_124_number():
    assert make_124_number(1) == '1'
    assert make_124_number(2) == '2'
    assert make_124_number(3) == '4'
    assert make_124_number(4) == '11'
    assert make_124_number(5) == '12'
    assert make_124_number(6) == '14'
    assert make_124_number(7) == '21'
    assert make_124_number(8) == '22'
    assert make_124_number(9) == '24'
    assert make_124_number(10) == '41'


"""
다른 풀이
"""
def change124(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]

