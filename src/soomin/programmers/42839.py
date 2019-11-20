import itertools
def solution(numbers):
    permutation = []
    counter_set = set()
    # str 조합 join 후 int 변환해서 set box에 넣기
    for i in range(1,len(numbers)+1):
        permutation = map(lambda x: int(''.join(x)) ,itertools.permutations(numbers,i))
        for i in permutation:
            if is_prime(i): counter_set.add(i)
    return len(counter_set)
            
def is_prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    return True