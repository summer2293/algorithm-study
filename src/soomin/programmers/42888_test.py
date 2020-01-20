import pytest
import collections
import re


@pytest.mark.parametrize("base, expected", [
    (["Enter uid1234 Muzi", 
      "Enter uid4567 Prodo",
      "Leave uid1234",
      "Enter uid1234 Prodo",
      "Change uid4567 Ryan"], 
      
      ["Prodo님이 들어왔습니다.", 
       "Ryan님이 들어왔습니다.", 
       "Prodo님이 나갔습니다.", 
       "Prodo님이 들어왔습니다."])
])


def test_simple(base, expected):
    assert solution(base) == expected


def solution(record):
    user = dict()
    answer = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    # user setting O(N)
    for timeline in record: 
        token = timeline.split(" ")
        try: user[token[1]] = token[2]
        except: pass

    # print message  O(N) 
    for timeline in record:
        token = timeline.split(" ")
        action, name = token[0], token[1]
        message = ""
        try:
            if action == "Enter" or "Leave":
                message += user[name]+messages[action]
        except: continue
        answer.append(message)
    return answer



if __name__ == "__main__":
    solution(base)

