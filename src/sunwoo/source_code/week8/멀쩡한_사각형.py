def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def solution(w, h):
    return w * h - w - h + gcd(w, h)

answer = solution(3, 3)
print(answer)

def gcd(a, b):
    return b if a == 0 else gcd((b % a), a)
