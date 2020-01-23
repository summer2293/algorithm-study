# [124 나라의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12899)

```python

def solution(n):
    answer = ''

    num_dict = {1:"1",2:"2",0:"4"}
    mok = 1
    na = 1
    
    while mok != 0:
        mok = n //3
        na = n % 3
        
        if na == 0 :
            mok -= 1
            
        n = mok
            
        answer = num_dict[na] + answer
    
    return answer

# 정확성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.6MB)
# 테스트 2 〉	통과 (0.04ms, 10.6MB)
# 테스트 3 〉	통과 (0.04ms, 10.6MB)
# 테스트 4 〉	통과 (0.04ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.8MB)
# 테스트 7 〉	통과 (0.05ms, 10.6MB)
# 테스트 8 〉	통과 (0.04ms, 10.6MB)
# 테스트 9 〉	통과 (0.04ms, 10.6MB)
# 테스트 10 〉	통과 (0.04ms, 10.7MB)
# 테스트 11 〉	통과 (0.04ms, 10.7MB)
# 테스트 12 〉	통과 (0.04ms, 10.7MB)
# 테스트 13 〉	통과 (0.04ms, 10.6MB)
# 테스트 14 〉	통과 (0.04ms, 10.7MB)
# 효율성  테스트
# 테스트 1 〉	통과 (0.04ms, 10.7MB)
# 테스트 2 〉	통과 (0.04ms, 10.8MB)
# 테스트 3 〉	통과 (0.04ms, 10.5MB)
# 테스트 4 〉	통과 (0.10ms, 10.7MB)
# 테스트 5 〉	통과 (0.04ms, 10.7MB)
# 테스트 6 〉	통과 (0.06ms, 10.7MB)
```


# [programmers-오픈채팅방](https://programmers.co.kr/learn/courses/30/lessons/42888)

```python

# 배열(맵) 
# record를 순회하면서
# Enter, Leave인 경우 유저 아이디와 함께 정답에 출력될 메세지의 종류를 기록해둡니다. 이렇게 기록해 둔 것을 : event
# Enter, Change인 경우 연관 배열을 이용하여 각 유저 아이디를 키로, 닉네임 값으로 저장. 최종 닉네임을 유저 아이디 별로 유지
# events를 순회하면서 채팅방에 출력할 메세지를 생성할 때, 연관 배열에 저장된 아이디 별 최종 닉네임을 이용

def solution(record):
    answer = []
    logs= []
    Dict = dict()

    for i in range(len(record)):
        events = record[i].split(" ")
        if events[0] == "Enter":
            Dict[events[1]] = events[2]
            logs.append([events[1],"님이 들어왔습니다."])

        elif events[0] == "Leave":
            logs.append([events[1],"님이 나갔습니다."])
        elif events[0] == "Change":
            Dict[events[1]] = events[2]

    for log in logs:
        Diction = Dict[log[0]]
        answer.append(Diction+log[1])

    return answer



# 정확성  테스트
# 테스트 1 〉	통과 (0.05ms, 10.8MB)
# 테스트 2 〉	통과 (0.05ms, 10.7MB)
# 테스트 3 〉	통과 (0.08ms, 10.7MB)
# 테스트 4 〉	통과 (0.07ms, 10.7MB)
# 테스트 5 〉	통과 (0.60ms, 11.1MB)
# 테스트 6 〉	통과 (0.68ms, 11.1MB)
# 테스트 7 〉	통과 (0.57ms, 11MB)
# 테스트 8 〉	통과 (0.92ms, 11MB)
# 테스트 9 〉	통과 (0.84ms, 11.1MB)
# 테스트 10 〉	통과 (0.73ms, 11.2MB)
# 테스트 11 〉	통과 (0.40ms, 11MB)
# 테스트 12 〉	통과 (0.38ms, 11MB)
# 테스트 13 〉	통과 (0.69ms, 11.1MB)
# 테스트 14 〉	통과 (0.82ms, 11.2MB)
# 테스트 15 〉	통과 (0.04ms, 10.7MB)
# 테스트 16 〉	통과 (0.05ms, 10.7MB)
# 테스트 17 〉	통과 (0.11ms, 10.7MB)
# 테스트 18 〉	통과 (0.10ms, 10.8MB)
# 테스트 19 〉	통과 (0.78ms, 11.1MB)
# 테스트 20 〉	통과 (0.59ms, 11MB)
# 테스트 21 〉	통과 (0.59ms, 11.1MB)
# 테스트 22 〉	통과 (0.58ms, 11MB)
# 테스트 23 〉	통과 (0.79ms, 11.2MB)
# 테스트 24 〉	통과 (0.83ms, 11.1MB)
# 테스트 25 〉	통과 (113.59ms, 159MB)
# 테스트 26 〉	통과 (110.34ms, 164MB)
# 테스트 27 〉	통과 (119.61ms, 166MB)
# 테스트 28 〉	통과 (124.51ms, 170MB)
# 테스트 29 〉	통과 (113.61ms, 170MB)
# 테스트 30 〉	통과 (90.87ms, 150MB)
# 테스트 31 〉	통과 (96.60ms, 146MB)
# 테스트 32 〉	통과 (90.95ms, 147MB)
```