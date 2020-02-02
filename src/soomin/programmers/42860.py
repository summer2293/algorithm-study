# 조이스틱 https://programmers.co.kr/learn/courses/30/lessons/42860
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def solution(name):
    answer =  0

    count = change_alphabet(name)     # 1. A 기준 자리 별 알파벳 움직여야할 숫자 횟수 계산! b > 1 c > 2 >

    # 2. 첫번째 위치 값 넣기 
    index = 0
    answer += count[index]
    count[index] = 0

    # 3. 다음에 움직일 값 찾기. 값을 돌면서 0으로 바꿔주고, sum 이 0 이되면 다 변경 한 것. 종료 
    while(sum(count) != 0):
        data  = find_next_index(index, count) # 현재 위치에서 0이 아닌 값 중 제일 가까운 index 와 최소 움직임 반환 
        index = data["index"]
        if index is not None: 
            answer += count[index] + data["move"]
            count[index] = 0
    return answer


def change_alphabet(name):
    alphabet =[]
    for char in name:
        idx = ALPHABET.index(char)
        alphabet.append(min(idx, len(ALPHABET) - idx))
    return alphabet


def find_next_index(idx, count):
    for num in range(len(count)):
        ascending, descending  = (num+idx)%len(count), (len(count)-num+idx) % len(count) # 1, 2, 3, 4 and 10, 9, 8, 7
        if count[ascending] != 0: return {"index":ascending, "move":num}
        if count[descending] != 0: return {"index":descending, "move":num}