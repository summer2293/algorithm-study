# 자릿수더하기 https://programmers.co.kr/learn/courses/30/lessons/12931
def digits_plus(n):
    sum_of_digit = 0
    for digit in str(n):
        sum_of_digit += int(digit)
    return sum_of_digit


def test_digits_plus():
    assert digits_plus(123) == 6
    assert digits_plus(987) == 24
    assert digits_plus(10002) == 3
