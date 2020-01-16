# 문자열 압축 : https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    
    if len(s)==1:
        return 1
    
    answer = len(s)
    
    half_len = int(len(s)/2)
    
    for i in range(1,half_len+1):
        start = i #now의 초기화
        res = [] #압축 결과
        pre_s = s[0:i]
        num = 1
        while True:
            now_s = s[start:start+i]
            if now_s == pre_s:
                num += 1
            else : 
                res.append([num, pre_s])
                num = 1
                pre_s = now_s
            if start > len(s):
                break
            start += i
            
        half_len = 0
        
        for j in range(len(res)):
            if res[j][0] == 1:
                half_len += len(res[j][1])
            else :
                half_len += len(str(res[j][0]))
                half_len += len(res[j][1])
        
        answer = min(answer, half_len)
    return answer


# 테스트 1 〉	통과 (0.09ms, 10.7MB)
# 테스트 2 〉	통과 (0.51ms, 10.7MB)
# 테스트 3 〉	통과 (0.27ms, 10.7MB)
# 테스트 4 〉	통과 (0.07ms, 10.6MB)
# 테스트 5 〉	통과 (0.03ms, 10.7MB)
# 테스트 6 〉	통과 (0.09ms, 10.8MB)
# 테스트 7 〉	통과 (0.57ms, 10.7MB)
# 테스트 8 〉	통과 (0.61ms, 10.7MB)
# 테스트 9 〉	통과 (0.84ms, 10.7MB)
# 테스트 10 〉	통과 (3.05ms, 10.7MB)
# 테스트 11 〉	통과 (0.15ms, 10.7MB)
# 테스트 12 〉	통과 (0.15ms, 10.7MB)
# 테스트 13 〉	통과 (0.17ms, 10.7MB)
# 테스트 14 〉	통과 (0.82ms, 10.8MB)
# 테스트 15 〉	통과 (0.17ms, 10.7MB)
# 테스트 16 〉	통과 (0.05ms, 10.8MB)
# 테스트 17 〉	통과 (2.82ms, 10.7MB)
# 테스트 18 〉	통과 (1.43ms, 10.7MB)
# 테스트 19 〉	통과 (1.45ms, 10.7MB)
# 테스트 20 〉	통과 (3.39ms, 10.7MB)
# 테스트 21 〉	통과 (3.29ms, 10.7MB)
# 테스트 22 〉	통과 (3.30ms, 10.7MB)
# 테스트 23 〉	통과 (3.27ms, 10.8MB)
# 테스트 24 〉	통과 (3.07ms, 10.7MB)
# 테스트 25 〉	통과 (3.36ms, 10.8MB)
# 테스트 26 〉	통과 (3.16ms, 10.7MB)
# 테스트 27 〉	통과 (3.25ms, 10.6MB)
# 테스트 28 〉	통과 (0.05ms, 10.8MB)