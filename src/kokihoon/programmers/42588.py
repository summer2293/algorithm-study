def solution(heights):
    heights = heights[::-1]
    length = len(heights)
    check = False
    answer = []

    for i in range(len(heights)):
        for j in range(i, len(heights)-1):
            if heights[i] < heights[j+1]:
                answer.append(length-j-1)
                check = True
                break
        if check == False:
            answer.append(0)
        else :
            check = False



    return answer[::-1]