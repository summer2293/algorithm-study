# 완주하지 못한 선수 https://programmers.co.kr/learn/courses/30/lessons/42576
def an_incomplete_player(p, c):
    completion = dict()
    for person in c:
        try:
            completion[person] += 1
        except:
            completion[person] = 1
    for person in p:
        try:
            completion[person] -= 1
            if completion[person] == -1:
                return person
        except:
            return person
    


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