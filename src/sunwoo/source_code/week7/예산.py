def solution(d, budget):
    d.sort()
    count = 0

    for price in d:
        budget -= price
        if budget < 0: return count
        else: count += 1

    return count

def solution2(d, budget):
    d.sort()
    for index, price in enumerate(d):
        budget -= price
        if budget < 0: return index



    return len(d)