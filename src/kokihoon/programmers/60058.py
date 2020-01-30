def solution(p):
    answer = ''
    v = ''
    if p == '' :
        return p

    left_count = 0
    right_count = 0
    check = True

    for i in range(len(p)):
        if p[i] == '(':
            left_count +=1
            answer += p[i]

        else :
            right_count +=1
            answer += p[i]
            if right_count > left_count :
                check = False
        if left_count == right_count:
            if check == True :
                return answer + solution(p[i+1:])
            else :

                return '(' + solution(p[i+1:]) + ')' + answer[1:-1][::-1]

    return answer
```