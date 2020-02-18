def fromstrint(strTime):
    return int(strTime[:2])*60 + int(strTime[3:])


def fromintstr(intTime):
    return str(intTime // 60).zfill(2) + ":" + str(intTime % 60).zfill(2)

def solution(n, t, m, timetable):
    busTime = []
    for i in range(n):
        time = t*i
        busTime.append(540+time)
    inttimetable = []
    timetable.sort()
    for i in timetable:
        inttimetable.append(fromstrint(i))
    count = 0
    while len(busTime) != 1:
        if not inttimetable:
            break
        elif count == m or busTime[0] < inttimetable[0]:
            count =0
            busTime.pop(0)
        elif busTime[0] >= inttimetable[0]:
            inttimetable.pop(0)
            count += 1
            
    if len(inttimetable) < m:
        answer = fromintstr(busTime[0])
    else:
        for i in range(busTime[0], -1, -1):
            inttimetable.append(i+0.1)
            inttimetable.sort()
            if i+0.1 in inttimetable[0:m]:
                answer = fromintstr(i)
                break
            else:
                inttimetable.remove(i+0.1)
    return answer