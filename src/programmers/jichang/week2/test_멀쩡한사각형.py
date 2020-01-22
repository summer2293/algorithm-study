"""
솔루션을 봤음
"""

from math import gcd

def available_square(W, H):
    return W * H - W - H + gcd(W, H)


def test_available_square():
    assert available_square(8, 12) == 80
    assert available_square(2, 3) == 2
    assert available_square(4, 6) == 16
    assert available_square(5, 7) == 24
    assert available_square(3, 7) == 12
    assert available_square(5, 5) == 20
    assert available_square(10, 20) == 200 - 20
