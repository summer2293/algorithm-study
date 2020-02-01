# https://programmers.co.kr/learn/courses/30/lessons/62048
from fractions import Fraction
def solution(w, h):
    if w == h:
        return w ** 2 - w

    frac = Fraction(w,h)
    new_w = frac.numerator
    new_h = frac.denominator
    num_split =  new_w + new_h - 1
    # print(num_split, "num split")
    num_rectangles = w // new_w
    # print(num_rectangles, "num recta")
    return w * h - num_rectangles * num_split 


print(solution(8,12))
# space complexity: 1
# time complexity: log(n) for fractionizing -> gcd



# some other guy's solution
# def gcd(a, b): return b if (a == 0) else gcd(b % a, a)
# def solution(w, h): return w*h-w-h+gcd(w, h)
