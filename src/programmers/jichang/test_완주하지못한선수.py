# 완주하지 못한 선수 https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter

def an_incomplete_player(p, c):
    """참가자와 완주한 사람의 목록이 주어지고 완주하지 못한 선수를 구한다.

    시간 복잡도:
    p의 길이를 n이라고 할 때 O(p)
    """
    return list((Counter(p) - Counter(c)).keys())[0]


def test_an_incomplete_player():
    assert an_incomplete_player(["leo", "kiki", "eden"],
                                ["eden", "kiki"])\
        == "leo"
    assert an_incomplete_player(["marina", "josipa", "nikola", "vinko", "filipa"],
                                ["josipa", "filipa", "marina", "nikola"])\
        == "vinko"
    assert an_incomplete_player(["mislav", "stanko", "mislav", "ana"],
                                ["stanko", "ana", "mislav"])\
        == "mislav"
