# 개선 코드 (다른사람 풀이 보고 )
def solution(record):
    user = dict()
    answer = []
    tokens = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    
    # user setting O(N)
    for timeline in record: 
        token = timeline.split(" ")
        try: user[token[1]] = token[2]
        except: pass
        tokens.append(token)

    # print message  O(N) 
    for token in tokens:
        action, name = token[0], token[1]
        message = ""
        try:
            if action == "Enter" or "Leave":
                message += user[name]+messages[action]
        except: continue
        answer.append(message)
    return answer

# 원래 코드

def solution(record):
    user = dict()
    tokens = []
    answer = []
    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    # part token O(N)
    for timeline in record: 
        tokens.append(timeline.split(" "))

    # user uid setting O(N)
    for token in tokens:
        try: user[token[1]] = token[2]
        except: pass

    # print message  O(N) 
    for token in tokens:
        action = token[0]
        name = token[1]
        message = ""
        if action == "Enter":
            message += "{nickname}님이 들어왔습니다.".format(nickname=user[name])
        elif action == "Leave":
            message += "{nickname}님이 나갔습니다.".format(nickname=user[name])
        else: continue
        answer.append(message)
    return answer