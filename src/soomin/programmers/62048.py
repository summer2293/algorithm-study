# 멀쩡한 사각형
# dp 
def solution(w,h):
    answer = 0
    short, long = min(w,h), max(w,h) # O(N)
    while (short != 0): 
        if short == 1:
            answer += 0 
            break
        count, long = long//short, long%short
        answer += (short * short - short) * count
        short, long = min(short,long), max(short,long)
    return answer