def solution(record):
    answer = []

    dict = {}

    for i in range(len(record)):
        if record[i][0] != 'L' :
            x,y,z = record[i].split(' ')
            dict[y] = z

    for i in range(len(record)):
        if record[i][0] == 'E':
            x,y,z = record[i].split(' ')
            answer.append(dict[y]+'님이 들어왔습니다.')
        elif record[i][0] == 'L' :
            x, y = record[i].split(' ')
            answer.append(dict[y]+'님이 나갔습니다.')

    return answer