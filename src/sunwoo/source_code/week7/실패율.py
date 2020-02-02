def solution(N, stages):
    counter = len(stages)
    rates = []
    for i in range(1, N+1):
        if N >= i and counter > 0:
            rates.append(((i,float(stages.count(i) / counter))))
            counter = counter - stages.count(i)
        else:
            rates.append((i, 0))

    sorted_stage_rates = sorted(rates, key=lambda rate: rate[1], reverse=True)
    return list(map(lambda rate: rate[0], sorted_stage_rates))[:N]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))