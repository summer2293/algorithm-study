# -*- coding: utf-8 -*-

def solution(record):
    myID = record[0].split()[1]

    enter_message = "{}님이 들어왔습니다."
    exit_message = "{}님이 나갔습니다."

    users = {}
    answer = []

    for log in record:
        split = log.split()

        if split[0] == "Enter":
            users[split[1]] = split[2]
            if split[1] == myID or users[split[1]] == None: continue
            answer.append(enter_message.format(split[2]))

        elif split[0] == "Leave" and split[1] != myID:

            users[split[1]] = None
            if split[1] == myID or users[split[1]] == None: continue
            answer.append(exit_message.format(users[split[1]]))

        elif split[0] == "Change":
            if users[split[1]] == None:
                users[split[1]] = split[2]
                continue
            oldName = users[split[1]]
            answer.append(enter_message.format(split[2]))
            users[split[1]] = split[2]
            answer.append(exit_message.format(oldName))
            answer.append(enter_message.format(oldName))

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))