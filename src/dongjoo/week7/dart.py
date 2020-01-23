def solution(dartResult):
    if not dartResult:
        return 0

    points = []
    exponents = []
    bonuses = []

    # parse string into appropriate arrays
    for i in range(len(dartResult)):
        # logic for points
        if dartResult[i].isnumeric():
            if i + 1 < len(dartResult) and dartResult[i+1] == '0':
                    points.append(10)
            elif dartResult[i-1] == '1':
                continue
            else:
                points.append(int(dartResult[i]))
        # logic for exponents
        elif dartResult[i].isalpha():
            exponents.append(dartResult[i])

            # logic for bonuses, * and #
            # for cases with bonuses
            if i + 1 < len(dartResult) and not dartResult[i+1].isalnum():
                bonuses.append(dartResult[i+1])
            # for cases with no bonuses
            else:
                bonuses.append(None)


    #calculate points
    answer = 0
    prev_point = 0
    for i in range(len(points)):
        curr_point = points[i]
        # exponent part
        if exponents[i] == "D":
            curr_point = curr_point ** 2
        elif exponents[i] == "T":
            curr_point = curr_point ** 3
        # bonus part
        if bonuses[i] == None:
            pass
        elif bonuses[i] == "*":
            if i == 0:
                curr_point *= 2
            else:
                curr_point *= 2
                # adding prev_point one more time is same as doubling prev_point and adding it
                answer += prev_point
        elif bonuses[i] == "#":
            curr_point *= -1

        answer += curr_point
        prev_point = curr_point
    return answer

# time & space complexity: linear

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
