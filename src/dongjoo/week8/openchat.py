# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    # arr to keep track of entering/exit order and ID
    # 1st element: 1 for enter 0 for exit, 2nd element: uid
    enter_exit_id = []
    entered_message = "님이 들어왔습니다."
    exit_message = "님이 나갔습니다."
    # dictionary to keep track of  key: user id, value: most recent nickname
    user_dict = dict()
    answer = []

    # change_count = 0

    for message in record:
        # print(enter_exit_id, i, "enter exit, id")
        action = message.split(' ')
        if action[0] == 'Enter':
            enter_exit_id.append([1, action[1]])
            user_dict[action[1]] = action[2]
        elif action[0] == 'Leave':
            enter_exit_id.append([0, action[1]])
        else:
            user_dict[action[1]] = action[2]
            # change_count += 1

    for log in enter_exit_id:
        message = ""
        if log[0]:
            message = user_dict[log[1]] + entered_message
        else:
            message = user_dict[log[1]] + exit_message
        answer.append(message)

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))


# fixed size array를 미리 선언해서 optimize 해보려고 했으나 에러 나서 그냥 쉽게 함, 밑에는 틀린 코드
# 로직은 같은데 뭐가 틀렸을까?

# def solution(record):
#     # arr to keep track of entering/exit order and ID
#     # 1st element: 1 for enter 0 for exit, 2nd element: uid
#     enter_exit_id = [[0, "uid"]] * len(record)
#     entered_message = "님이 들어왔습니다."
#     exit_message = "님이 나갔습니다."
#     # dictionary to keep track of  key: user id, value: most recent nickname
#     user_dict = dict()
#     answer = [""] * len(record)

#     change_count = 0

#     for i in range(len(record)):
#         # print(enter_exit_id, i, "enter exit, id")
#         action = record[i].split(' ')
#         if action[0] == 'Enter':
#             enter_exit_id[i] = [1, action[1]]
#             user_dict[action[1]] = action[2]
#         elif action[0] == 'Leave':
#             enter_exit_id[i] = [0, action[1]]
#         else:
#             user_dict[action[1]] = action[2]
#             change_count += 1

#     for i in range(len(enter_exit_id) - change_count):
#         message = ""
#         if enter_exit_id[i][0]:
#             message = user_dict[enter_exit_id[i][1]] + entered_message
#         else:
#             message = user_dict[enter_exit_id[i][1]] + exit_message
#         answer[i] = message

#     return answer[:len(answer)-change_count]


# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo",
#                 "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
